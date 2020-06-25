#
# Conditional build:
%bcond_with	static_libs	# static library
#
Summary:	A RDP viewer widget for GTK+
Summary(pl.UTF-8):	Widżet przeglądarki RDP dla GTK+
Name:		gtk-frdp
Version:	3.37.1
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://gitlab.gnome.org/GNOME/gtk-frdp/-/tags
Source0:	https://gitlab.gnome.org/GNOME/gtk-frdp/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# Source0-md5:	ffabe0f8269194ebe8e05845eeec8fcd
URL:		https://gitlab.gnome.org/GNOME/gtk-frdp
BuildRequires:	freerdp2-devel >= 2
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	meson >= 0.40.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vala
Requires:	glib2 >= 1:2.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-frdp is a RDP viewer widget powered by FreeRDP and GTK+, developed
initially to be used in GNOME Boxes.

%description -l pl.UTF-8
gtk-frdp to widżet przeglądarki RDP, oparty o biblioteki FreeRDP i
GTK+, powstały początkowo na potrzeby GNOME Boxes.

%package devel
Summary:	Header files for gtk-frdp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-frdp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50

%description devel
Header files for gtk-frdp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-frdp.

%package static
Summary:	Static gtk-frdp library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-frdp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-frdp library.

%description static -l pl.UTF-8
Statyczna biblioteka gtk-frdp.

%package -n vala-gtk-frdp
Summary:	Vala API for gtk-frdp library
Summary(pl.UTF-8):	API języka Vala do biblioteki gtk-frdp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description -n vala-gtk-frdp
Vala API for gtk-frdp library.

%description -n vala-gtk-frdp -l pl.UTF-8
API języka Vala do biblioteki gtk-frdp.

%prep
%setup -q -n %{name}-v%{version}

%if %{with static_libs}
%{__sed} -i -e '/^gtk_frdp_lib = / s/shared_library/library/' src/meson.build
%endif

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-frdp-0.1.so
%{_libdir}/girepository-1.0/GtkFrdp-0.1.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/gtk-frdp
%{_datadir}/gir-1.0/GtkFrdp-0.1.gir
%{_pkgconfigdir}/gtk-frdp-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-frdp-0.1.a
%endif

%files -n vala-gtk-frdp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gtk-frdp-0.1.deps
%{_datadir}/vala/vapi/gtk-frdp-0.1.vapi
