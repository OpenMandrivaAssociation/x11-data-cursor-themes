Name: x11-data-cursor-themes
Version: 1.0.1
Release: %mkrel 6
BuildArch: noarch
Summary: X11 Cursor Themes
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/data/xcursor-themes-%{version}.tar.bz2 
Source1: wonderland-cursor.tar.bz2
Source2: index.theme
Source3: contrastlarge.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: xcursorgen >= 1.0.0
BuildRequires: libxcursor-devel >= 1.1.5.2

Conflicts: xorg-x11 < 7.0

%description
X11 Cursor Themes

%prep
%setup -q -n xcursor-themes-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

tar xjv -C %{buildroot}%{_iconsdir} -f %{SOURCE1} 
tar xjv -C %{buildroot}%{_iconsdir} -f %{SOURCE3} 
mkdir -p %{buildroot}/%{_iconsdir}/default
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/default

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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


