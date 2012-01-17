%define		sname	fuse

Name:		fuse-emulator
Version:	1.0.0.1a
Release:	%mkrel 2
Summary:	Free Unix Spectrum Emulator
License:	GPLv2+
Group:		Emulators
URL:		http://fuse-emulator.sourceforge.net/
Source0:	%{sname}-%{version}.tar.gz
Source1:	%{sname}-icons.tar.bz2
Patch0:		fuse-1.0.0.1a-zlib.patch
BuildRequires:	jsw-devel
BuildRequires:	libxml2-devel
BuildRequires:	libspectrum-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	gtk+2-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	png-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl
BuildRequires:	autoconf

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

%prep
%setup -q -n %{sname}-%{version}
%setup -q -T -D -a1 -n %{sname}-%{version}
%patch0 -p1

%build
autoreconf
%configure --with-gtk2 --with-roms-dir=%{_datadir}/%{sname}
%make

%install
%__rm -rf %{buildroot}
%makeinstall
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat<<EOF>%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Fuse
Comment=Free Unix Spectrum Emulator
Exec=%{_bindir}/%{sname}
Icon=%{sname}
Terminal=false
Type=Application
Categories=Game;Emulator;X-MandrivaLinux-MoreApplications-Emulators;
EOF
%__install -D -m 644 %{sname}48.png %{buildroot}%{_liconsdir}/%{sname}.png
%__install -D -m 644 %{sname}32.png %{buildroot}%{_iconsdir}/%{sname}.png
%__install -D -m 644 %{sname}16.png %{buildroot}%{_miconsdir}/%{sname}.png

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README THANKS COPYING AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{sname}*
%{_iconsdir}/%{sname}*
%{_liconsdir}/%{sname}*
%{_mandir}/*/*
%{_datadir}/%{sname}

