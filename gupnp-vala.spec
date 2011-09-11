# NOTE: it's gupnp-vala.spec to allow having vala-gupnp as subpackage
#
# Conditional build:
%bcond_without	tests	# don't build tests
#
Summary:	Vala bindings to GUPnP libraries
Summary(pl.UTF-8):	Wiązania języka Vala do bibliotek GUPnP
Name:		gupnp-vala
# note: 0.8.x is stable, 0.9.x unstable
Version:	0.8.0
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
#Source0Download: http://gupnp.org/download
Source0:	http://gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9d5d15ca5b540289552a9504f9f9c0f3
Patch0:		%{name}-notests.patch
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gssdp-devel >= 0.9.2
BuildRequires:	gupnp-av-devel >= 0.7.0
BuildRequires:	gupnp-devel >= 0.13.3
BuildRequires:	gupnp-dlna-devel >= 0.5.1
BuildRequires:	gupnp-ui-devel >= 0.1.1
BuildRequires:	pkgconfig
%{?with_tests:BuildRequires:	vala >= 0.11.3}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vala bindings to GUPnP libraries.

%description -l pl.UTF-8
Wiązania języka Vala do bibliotek GUPnP.

%package -n vala-gssdp
Summary:	Vala binding for GSSDP library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GSSDP
Group:		Development/Libraries
Requires:	gssdp-devel >= 0.9.2
Requires:	vala >= 0.11.3

%description -n vala-gssdp
Vala binding for GSSDP library.

%description -n vala-gssdp -l pl.UTF-8
Wiązanie języka Vala do biblioteki GSSDP.

%package -n vala-gupnp
Summary:	Vala binding for GUPnP library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP
Group:		Development/Libraries
Requires:	gupnp-devel >= 0.13.3
Requires:	vala-gssdp = %{version}-%{release}

%description -n vala-gupnp
Vala binding for GUPnP library.

%description -n vala-gupnp -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP.

%package -n vala-gupnp-av
Summary:	Vala binding for GUPnP AV library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP AV
Group:		Development/Libraries
Requires:	gupnp-av-devel >= 0.7.0
Requires:	vala-gupnp = %{version}-%{release}

%description -n vala-gupnp-av
Vala binding for GUPnP AV library.

%description -n vala-gupnp-av -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP AV.

%package -n vala-gupnp-dlna
Summary:	Vala binding for GUPnP DLNA library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP DLNA 
Group:		Development/Libraries
Requires:	gupnp-dlna-devel >= 0.5.1
Requires:	vala-gupnp = %{version}-%{release}

%description -n vala-gupnp-dlna
Vala binding for GUPnP DLNA library.

%description -n vala-gupnp-dlna -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP DLNA.

%package -n vala-gupnp-ui
Summary:	Vala binding for GUPnP-UI library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP-UI 
Group:		Development/Libraries
Requires:	gupnp-ui-devel >= 0.1.1
Requires:	vala-gupnp = %{version}-%{release}

%description -n vala-gupnp-ui
Vala binding for GUPnP-UI library.

%description -n vala-gupnp-ui -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP-UI.

%prep
%setup -q
%{!?with_tests:%patch0 -p1}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n vala-gssdp
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_datadir}/vala/vapi/gssdp-1.0.deps
%{_datadir}/vala/vapi/gssdp-1.0.vapi
%{_pkgconfigdir}/gupnp-vala-1.0.pc

%files -n vala-gupnp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-1.0.deps
%{_datadir}/vala/vapi/gupnp-1.0.vapi

%files -n vala-gupnp-av
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi

%files -n vala-gupnp-dlna
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-dlna-1.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-1.0.vapi

%files -n vala-gupnp-ui
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-ui-1.0.deps
%{_datadir}/vala/vapi/gupnp-ui-1.0.vapi
