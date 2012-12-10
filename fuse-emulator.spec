%define		sname	fuse

Name:		fuse-emulator
Version:	1.0.0.1a
Release:	3
Summary:	Free Unix Spectrum Emulator
License:	GPLv2+
Group:		Emulators
URL:		http://fuse-emulator.sourceforge.net/
Source0:	%{sname}-%{version}.tar.gz
Source1:	%{sname}-icons.tar.bz2
Patch0:		fuse-1.0.0.1a-zlib.patch
BuildRequires:	jsw-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	libspectrum-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(alsa)
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
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
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



%changelog
* Tue Jan 17 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.0.1a-2mdv2011.0
+ Revision: 762009
- Add patch0 to fix build, update BuildRequires
- Fix rom path in configure options, spec cleanup

* Wed Jul 27 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.0.1a-1
+ Revision: 691949
- Try to fix menus issue
- Rebuild
- Fix BuildRequires
- imported package fuse-emulator


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.0.0.1a-1mdv2011.0
- New version 1.0.0.1a
- Fix .desktop
- Import from PLF
- Remove PLF reference

* Sat Jan 17 2009 Guillaume Bedot <littletux@zarb.org> 0.10.0.2-1plf2009.1
- 0.10.0.2
- build requires
- fix build with old jsw package

* Thu Jan  8 2009 Guillaume Bedot <littletux@zarb.org> 0.10.0.1-1plf2009.1
- 0.10.0.1

* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.9.0-1plf2008.1
- 0.9.0

* Mon May 14 2007 Guillaume Bedot <littletux@zarb.org> 0.8.0.1-1plf2008.0
- 0.8.0.1

* Wed May  2 2007 Guillaume Bedot <littletux@zarb.org> 0.8.0-1plf2008.0
- 0.8.0
- drop obsolete patch
- fix build (jsw / stdc++)

* Wed Jul 19 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-7plf2007.0
- xdg menu
- obsoletes / conflicts with old fuse package

* Wed Mar 15 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-6plf
- use mkrel

* Wed Mar 15 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-5plf
- renamed the package since a fuse package now exist in main

* Fri Nov 4 2005 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.7.0-4plf
- added patch to fix compile errors in sound.c with gcc 4

* Wed Feb 16 2005 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.7.0-3plf
- built against new lib765 library major version

* Sun Sep 26 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.7.0-2plf
- changed section Applications/Emulators into More Applications/Emulators

* Mon Jul 19 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.7.0-1plf
- new version

* Sun May 9 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.6.2.1-1plf
- introduce in PLF
- new version
- changed spec file to meet Mandrake's skel.spec
- repackaged icons
- repackaged sources into bz2 format
- removed XFree86 from BuildRequires (redundant), added libjsw-devel
- updated description and summary
- build for GTK2

* Wed Jan  7 2004 Olivier Thauvin <nanardon@klama.mandrake.org> 0.6.1.1-5mdk
- rebuild
- DIRM fix

* Mon Dec 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6.1.1-4mdk
- cleanup
- contrib introduction

* Wed Nov 5 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.1.1-3mdk
- changed the size of normal icon to 32x32 pixels
- icons repackaged into a single tar.bz2 archive
- added bison to BuildRequires

* Sat Nov 1 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.1.1-2mdk
- added normal and large sized icons
- made some fixes and cosmetic changes to the spec file

* Thu Sep 2 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.1.1-1mdk
- new version
- added libgcrypt1-devel to BuildRequires
- changed libspectrum0-devel into libspectrum2-devel in BuildRequires

* Wed Jun 4 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0.1-1mdk
- version update (security fix)

* Wed May 28 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-4mdk
- added icon

* Thu May 22 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-3mdk
- added BuildRequires

* Tue May 20 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-2mdk
- fixed xml support so configuration saving is now available

* Sun Apr 27 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-1mdk
- new version

* Thu Apr 24 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.5.1-1mdk
- first version of the package
- spec file written using Mandrake RPM HOWTO 1.1.1
