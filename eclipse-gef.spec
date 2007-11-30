# TODO
# - build from source
# - noarch
%define		buildid	200706281000
Summary:	Graphical Editing Framework
Summary(pl.UTF-8):	Graphical Editing Framework - środowisko do edycji graficznej
Name:		eclipse-gef
Version:	3.3
Release:	0.1
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/gef/downloads/drops/R-%{version}-%{buildid}/GEF-SDK-%{version}.zip
# Source0-md5:	4617aa14d4af15714679f9175d5d9e73
URL:		http://www.eclipse.org/gef/
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir	%{_libdir}/eclipse

%description
Graphical Editing Framework.

%description -l pl.UTF-8
Graphical Editing Framework - środowisko do edycji graficznej.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -a eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -a eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/org.eclipse.gef*
%{_eclipsedir}/plugins/org.eclipse.gef*
%{_eclipsedir}/plugins/org.eclipse.draw2d*
