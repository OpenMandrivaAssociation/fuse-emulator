%define		sname	fuse

Summary:	Free Unix Spectrum Emulator
Name:		fuse-emulator
Version:	1.1.1
Release:	4
License:	GPLv2+
Group:		Emulators
Url:		http://fuse-emulator.sourceforge.net/
Source0:	%{sname}-%{version}.tar.gz
Source1:	%{sname}-icons.tar.bz2
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	jsw-devel
BuildRequires:	libspectrum-devel >= %{version}
BuildRequires:	libgcrypt-devel >= 1.1.42
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

%build
autoreconf -fi
%configure2_5x \
	--enable-gtk2 \
	--with-roms-dir=%{_datadir}/%{sname}
%make

%install
%makeinstall_std

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


