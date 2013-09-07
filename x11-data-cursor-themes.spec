Summary:	X11 Cursor Themes
Name:		x11-data-cursor-themes
Version:	1.0.4
Release:	1
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/data/xcursor-themes-%{version}.tar.bz2 
Source1:	wonderland-cursor.tar.bz2
Source2:	index.theme
Source3:	contrastlarge.tar.bz2
BuildArch:	noarch
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	xcursorgen >= 1.0.0
BuildRequires:	pkgconfig(xcursor) >= 1.1.5.2
Conflicts:	xorg-x11 < 7.0

%description
Cursor themes for X11 environment.

%prep
%setup -q -n xcursor-themes-%{version}

%build
./configure --prefix=%{_prefix}
%make

%install
%makeinstall_std

tar xvj -C %{buildroot}%{_iconsdir} -f %{SOURCE1} 
tar xvj -C %{buildroot}%{_iconsdir} -f %{SOURCE3} 
mkdir -p %{buildroot}/%{_iconsdir}/default
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/default

# The contrastlarge "xterm" cursor is completly black, making it useless on a
# dark background, but the theme authors provide an alternative:
# xterm_extra_large
mv %{buildroot}/%{_iconsdir}/contrastlarge/cursors/xterm_extra_large %{buildroot}/%{_iconsdir}/contrastlarge/cursors/xterm

# Create Hash symlinks
THEMES="contrastlarge handhelds redglass whiteglass wonderland"
LINKS="00008160000006810000408080010102=sb_v_double_arrow \
028006030e0e7ebffc7f7070c0600140=sb_h_double_arrow \
03b6e0fcb3499374a867c041f52298f0=crossed_circle \
08e8e1c95fe2fc01f976f1e063a24ccd=left_ptr_watch \
14fef782d02440884392942c11205230=h_double_arrow	\
2870a09082c103050810ffdffffe0204=v_double_arrow \
3ecb610c1bf2410f44200f48c40d3599=left_ptr_watch \
4498f0e0c1937ffe01fd06f973665830=fleur \
5c6cd98b3f3ebcb1f9c7f1c204630408=question_arrow \
6407b0e94181790501fd1e167b474872=copy \
640fb0e74195791501fd1ed57b41487f=link \
9d800788f1b08800ae810202380a0822=hand1 \
c7088f0f3e6c8088236ef8e1e3e70000=top_left_corner \
d9ce0ab605698f320427677b458ad60b=question_arrow \
e29285e634086352946a0e7090d73106=hand2 \
fcf1c3c7cd4491d801f1e1c78f100000=top_right_corner"

for theme in $THEMES; do
    pushd %{buildroot}/%{_iconsdir}/$theme/cursors

    for link in $LINKS; do
    	from=`echo $link | cut -d= -f1`
    	to=`echo $link | cut -d= -f2`

    	if [ -e "$to" ] && [ ! -e "$from" ]; then
	   ln -s "$to" "$from"
	fi
    done

    popd
done

%files
# contrastlarge theme files have +x permission, undo this:
%doc ChangeLog README
%dir %{_datadir}/icons/default
%dir %{_datadir}/icons/handhelds
%dir %{_datadir}/icons/redglass
%dir %{_datadir}/icons/whiteglass
%dir %{_datadir}/icons/wonderland
%dir %{_datadir}/icons/contrastlarge
%{_datadir}/icons/default/*
%{_datadir}/icons/handhelds/*
%{_datadir}/icons/redglass/*
%{_datadir}/icons/whiteglass/*
%{_datadir}/icons/wonderland/*
%{_datadir}/icons/contrastlarge/*


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1.0.3-2mdv2011.0
+ Revision: 672452
- fix build
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Fri Jul 23 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 557297
- Replace xterm cursor for one that is not completely black (#41351)
- Fix file permissions
  CCBUG: 41351

* Wed Nov 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 465052
- spec file clean
- add better description
- add docs
- update to new version 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-8mdv2009.1
+ Revision: 351427
- rebuild

* Mon Jul 14 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.0.1-7mdv2009.0
+ Revision: 235630
- Create cursor hash symlinks. Fix bug #24950.

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 225940
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2008.1
+ Revision: 129524
- kill re-definition of %%buildroot on Pixel's request


* Thu Mar 01 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-5mdv2007.0
+ Revision: 130846
- added contrastlarge cursor theme to the package. (#9287)
- rebuild to fix cooker uploading
- increment release
- Adding X.org 7.0 to the repository

  + Frederic Crozat <fcrozat@mandriva.com>
    - Fix release
    - Add source1: wonderland cursors (new version)
      Add source2: default cursors are wonderland ones

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

