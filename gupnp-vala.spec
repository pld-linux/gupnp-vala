# OBSOLETE spec, see individual {gssdp,gupnp,gupnp-av,gupnp-dlna}.spec for current Vala bindings
# NOTE: it's gupnp-vala.spec to allow having vala-gupnp as subpackage
#
# Conditional build:
%bcond_without	tests		# don't build tests
%bcond_without	vala_gssdp	# use vala-gssdp from gssdp 0.12.2+
%bcond_without	gupnp		# gupnp binding (will be included in gupnp >= 0.19.0)
%bcond_without	gupnp_av	# gupnp-av binding (will be included in gupnp-av >= 0.11.0)
#
Summary:	Vala bindings to GUPnP libraries
Summary(pl.UTF-8):	Wiązania języka Vala do bibliotek GUPnP
Name:		gupnp-vala
# note: 0.10.x is stable, 0.11.x unstable
Version:	0.10.5
Release:	1.1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-vala/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	ab35180fccaa52dc30859f62f66edac1
Patch0:		%{name}-notests.patch
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	gssdp-devel >= 0.12.0
%if %{with gupnp_av}
BuildRequires:	gupnp-av-devel >= 0.10.0
BuildRequires:	gupnp-av-devel < 0.11.0
%endif
%if %{with gupnp}
BuildRequires:	gupnp-devel >= 0.18.0
BuildRequires:	gupnp-devel < 0.19.0
%endif
BuildRequires:	gupnp-dlna-devel >= 0.6.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
%{?with_tests:BuildRequires:	vala >= 0.11.3}
BuildRequires:	xz
%if %{with vala_gssdp}
BuildRequires:	vala-gssdp >= 0.12.2
%else
BuildRequires:	gssdp-devel < 0.12.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vala bindings to GUPnP libraries.

%description -l pl.UTF-8
Wiązania języka Vala do bibliotek GUPnP.

%package -n vala-gssdp
Summary:	Vala binding for GSSDP library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GSSDP
Group:		Development/Libraries
Requires:	gssdp-devel >= 0.12.0
Requires:	vala >= 0.11.3

%description -n vala-gssdp
Vala binding for GSSDP library.

%description -n vala-gssdp -l pl.UTF-8
Wiązanie języka Vala do biblioteki GSSDP.

%package -n vala-gupnp
Summary:	Vala binding for GUPnP library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP
Group:		Development/Libraries
Requires:	gupnp-devel >= 0.18.0
Requires:	vala >= 0.11.3
%if %{with vala_gssdp}
Requires:	vala-gssdp >= 0.12.2
%else
Requires:	vala-gssdp = %{version}-%{release}
%endif
Obsoletes:	vala-gupnp-ui

%description -n vala-gupnp
Vala binding for GUPnP library.

%description -n vala-gupnp -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP.

%package -n vala-gupnp-av
Summary:	Vala binding for GUPnP AV library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP AV
Group:		Development/Libraries
Requires:	gupnp-av-devel >= 0.10.0
Requires:	vala-gupnp = %{version}-%{release}

%description -n vala-gupnp-av
Vala binding for GUPnP AV library.

%description -n vala-gupnp-av -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP AV.

%package -n vala-gupnp-dlna
Summary:	Vala binding for GUPnP DLNA library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP DLNA
Group:		Development/Libraries
Requires:	gupnp-dlna-devel >= 0.6.0
Requires:	vala-gupnp = %{version}-%{release}

%description -n vala-gupnp-dlna
Vala binding for GUPnP DLNA library.

%description -n vala-gupnp-dlna -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP DLNA.

%prep
%setup -q
%{!?with_tests:%patch0 -p1}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without vala_gssdp}
%files -n vala-gssdp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gssdp-1.0.deps
%{_datadir}/vala/vapi/gssdp-1.0.vapi
%endif

%if %{with gupnp}
%files -n vala-gupnp
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_datadir}/vala/vapi/gupnp-1.0.deps
%{_datadir}/vala/vapi/gupnp-1.0.vapi
%{_pkgconfigdir}/gupnp-vala-1.0.pc
%endif

%if %{with gupnp_av}
%files -n vala-gupnp-av
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi
%endif

%files -n vala-gupnp-dlna
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-dlna-1.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-1.0.vapi
