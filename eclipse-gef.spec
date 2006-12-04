Summary:	Graphical Editing Framework
Name:		eclipse-gef
Version:	3.2.1
Release:	0.1
License:	CPL
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/gef/downloads/drops/R-3.2.1-200609211617/GEF-ALL-%{version}.zip
# Source0-md5:	fcf6ea042c70a8628613924e1e227150
#URL:		
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_datadir}/eclipse

%description
Graphical Editing Framework.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/org.eclipse.gef*
%{_eclipsedir}/plugins/org.eclipse.gef*
%{_eclipsedir}/plugins/org.eclipse.draw2d*
