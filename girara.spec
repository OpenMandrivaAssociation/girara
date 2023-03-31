%define major	3
%define libname	%mklibname %{name}-gtk3_ %{major}
%define devname	%mklibname %{name}-gtk3 -d

Name:		girara
Version:	0.3.8
Release:	2
Summary:	Simple user interface library
Group:		Development/Other
License:	zlib
URL:		http://pwmt.org/projects/girara/
Source0:	https://github.com/pwmt/girara/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	doxygen
BuildRequires:	meson

%description
Girara is a library that implements a user interface that focuses on simplicity
and minimalism.

%package -n %{libname}
Summary:	Simple user interface library
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
Girara is a library that implements a user interface that focuses on simplicity
and minimalism.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{_lib}%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%package i18n
Summary:	Internationalization and locale data for %{name}
Group:		System/Libraries
BuildArch:	noarch

%description i18n
Internationalization and locale data for %{name}

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

#we don't want these
find %{buildroot} -name "*.a" -delete

# fcami - I wish upstream used a consistent naming scheme
%find_lang lib%{name}-gtk3-%{major}

%files i18n -f lib%{name}-gtk3-%{major}.lang

%files -n %{libname}
%license LICENSE
%doc AUTHORS README*
%{_libdir}/libgirara-gtk3.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/girara-gtk3.pc
%{_libdir}/libgirara-gtk3.so
