Summary:	X11 Cursor Themes
Name:		x11-data-cursor-themes
Version:	1.0.6
Release:	11
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
%autosetup -n xcursor-themes-%{version} -p1

%build
./configure --prefix=%{_prefix}
%make_build

%install
%make_install

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
    cd %{buildroot}/%{_iconsdir}/$theme/cursors

    for link in $LINKS; do
    	from=$(echo $link | cut -d= -f1)
    	to=$(echo $link | cut -d= -f2)

    	if [ -e "$to" ] && [ ! -e "$from" ]; then
	   ln -s "$to" "$from"
	fi
    done

    cd -
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

