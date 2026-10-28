%define		sname	fuse

Summary:	Free Unix Spectrum Emulator
Name:		fuse-emulator
Version:	1.1.1
Release:	6
License:	GPLv2+
Group:		Emulators
Url:		https://fuse-emulator.sourceforge.net/
Source0:	%{sname}-%{version}.tar.gz
Source1:	%{sname}-icons.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	libspectrum-devel >= %{version}
# libspectrum.h includes gcrypt.h. The spectrum devel package does not require it.
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(zlib)

%description
What Fuse does have:

* Working 16K/48K/128K/+2/+2A/+3 Speccy, Timex TC2048/TC2068 and
  Pentagon 128 emulation, running at true Speccy speed on any computer
  you're likely to try it on.
* Support for loading from .tzx files.
* Sound (on systems supporting the Open Sound System, SDL, or OpenBSD/
  Solaris's /dev/audio).
* Emulation of most of the common joysticks used on the Spectrum
  (including Kempston, Sinclair and Cursor joysticks).
* Emulation of some of the printers you could attach to a Spectrum.
* Support for the RZX input recording file format, including
  'competition mode'.
* Emulation of the Spectrum +3e, ZXATASP and ZXCF IDE interfaces.

%files
%defattr(0644,root,root,0755)
%doc README THANKS COPYING AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{sname}*
%{_iconsdir}/%{sname}*
%{_liconsdir}/%{sname}*
%{_mandir}/*/*
%{_datadir}/%{sname}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{sname}-%{version}
%setup -q -T -D -a1 -n %{sname}-%{version}
# AM_PATH_GTK_2_0 and AM_PATH_XML2 compile a test program that does not
# link in the builders, so GTK is dropped and glib types disappear.
python - << 'PY'
from pathlib import Path
p = Path("configure.ac")
t = p.read_text()
old = """    elif test "$gtk3" = no; then
      AM_PATH_GTK_2_0(2.18.0,,
        AC_MSG_WARN([GTK+ not found. Reverting to Xlib])
        gtk=no
      )

    elif test "$gtk3" = auto; then
      AM_PATH_GTK_2_0(2.18.0,
        gtk3=no,
      )
"""
new = """    elif test "$gtk3" = no; then
      PKG_CHECK_MODULES([GTK], [gtk+-2.0 >= 2.18.0], [],
        [AC_MSG_WARN([GTK+ not found. Reverting to Xlib])
         gtk=no])

    elif test "$gtk3" = auto; then
      PKG_CHECK_MODULES([GTK], [gtk+-2.0 >= 2.18.0],
        [gtk3=no],
        [gtk3=auto])
"""
if old not in t:
    raise SystemExit("gtk block not found")
t = t.replace(old, new, 1)
old = """  AM_PATH_XML2(2.0.0,AC_DEFINE([HAVE_LIB_XML2], 1,
               [Defined if we've got libxml2]),
               AC_MSG_WARN(libxml2 not found - config file will use ini format))
"""
new = """  PKG_CHECK_MODULES([XML], [libxml-2.0 >= 2.0.0],
               [AC_DEFINE([HAVE_LIB_XML2], 1, [Defined if we have got libxml2])],
               [AC_MSG_WARN([libxml2 not found - config file will use ini format])])
"""
if old not in t:
    raise SystemExit("xml block not found")
t = t.replace(old, new, 1)
p.write_text(t)
PY
# --prefix=/usr adds -L/usr/lib. /usr/lib/libc.so is the 32-bit linker script.
sed -i 's|-L\$prefix/lib||' configure.ac

%build
autoreconf -fi
%configure2_5x \
	--with-roms-dir=%{_datadir}/%{sname}
# Generated libtool is a no-op after slibtoolize. Link with slibtool.
%make LIBTOOL=slibtool-shared

%install
%makeinstall_std LIBTOOL=slibtool-shared

mkdir -p %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Fuse
Comment=Free Unix Spectrum Emulator
Exec=%{_bindir}/%{sname}
Icon=%{sname}
Terminal=false
Type=Application
Categories=Game;Emulator;X-MandrivaLinux-MoreApplications-Emulators;
EOF

install -D -m 644 %{sname}48.png %{buildroot}%{_liconsdir}/%{sname}.png
install -D -m 644 %{sname}32.png %{buildroot}%{_iconsdir}/%{sname}.png
install -D -m 644 %{sname}16.png %{buildroot}%{_miconsdir}/%{sname}.png


