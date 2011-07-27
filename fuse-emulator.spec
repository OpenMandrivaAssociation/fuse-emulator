%define sname		fuse
Name:			fuse-emulator
Version:		1.0.0.1a
Release:		%mkrel 1

Summary:	Free Unix Spectrum Emulator
License:	GPLv2+
Group:		Emulators
URL:		http://fuse-emulator.sourceforge.net/
Source0:	%{sname}-%{version}.tar.gz
Source1:	%{sname}-icons.tar.bz2
#Patch0:		%{name}-0.10.0.1-plf-string-literal.patch

BuildRequires:	jsw-devel
BuildRequires:	libxml2-devel
BuildRequires:	libspectrum-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libgtk+2-devel 
BuildRequires:	libz-devel
BuildRequires:	libbzip2-devel
BuildRequires:	libpng-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	libalsa-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl
BuildRequires:	autoconf
BuildRoot:	%{_tmppath}/%{name}-%{version}

Obsoletes:	fuse <= 0.7.0-4plf
Conflicts:	fuse <= 0.7.0-4plf

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

This package is in PLF because it contains emulator related software.

%prep
%setup -q -n %{sname}-%{version}
%setup -q -T -D -a1 -n %{sname}-%{version}
#patch0 -p1 -b .string-literal

%build
autoreconf
%configure --with-gtk2
%make \
%if %mdkversion < 200910
LIBS="-ljsw -Wl,--no-as-needed -lstdc++"
%endif

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/%{_menudir}
cat<<EOF>%{buildroot}/%{_menudir}/%{name}
?package(%{name}): \
command="%{_bindir}/%{sname}" \
needs="X11" \
icon="%{sname}" \
section="More Applications/Emulators" \
title="Fuse" \
longtitle="Free Unix Spectrum Emulator" \
xdg="true"
EOF
mkdir -p %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Fuse
Comment=Free Unix Spectrum Emulator
Exec=%{_bindir}/%{sname}
Icon=%{sname}
Terminal=false
Type=Application
Categories=Game;Emulator;GTK;X-MandrivaLinux-MoreApplications-Emulators;
EOF
#__install -D -m 644 %{sname}48.png %{buildroot}%{_datadir}/pixmaps/%{sname}.png
%__install -D -m 644 %{sname}48.png %{buildroot}%{_liconsdir}/%{sname}.png
%__install -D -m 644 %{sname}32.png %{buildroot}%{_iconsdir}/%{sname}.png
%__install -D -m 644 %{sname}16.png %{buildroot}%{_miconsdir}/%{sname}.png

%if %mdkversion < 200900
%post
%update_menus

%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README THANKS COPYING AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_menudir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{sname}*
%{_iconsdir}/%{sname}*
%{_liconsdir}/%{sname}*
#{_datadir}/pixmaps/%{sname}.png
%{_mandir}/*/*
%{_datadir}/%{sname}

