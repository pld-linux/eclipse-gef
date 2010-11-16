%include	/usr/lib/rpm/macros.java
Summary:	Graphical Editing Framework
Summary(pl.UTF-8):	Graphical Editing Framework - środowisko do edycji graficznej
Name:		eclipse-gef
Version:	3.3.2
Release:	2
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/gef/downloads/drops/R-%{version}-200802211602/GEF-SDK-%{version}.zip
# Source0-md5:	a5770b033aa477c2c5742f27701926ad
URL:		http://www.eclipse.org/gef/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
Graphical Editing Framework.

%description -l pl.UTF-8
Graphical Editing Framework - środowisko do edycji graficznej.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a eclipse/features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a eclipse/plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.gef*
%{eclipsedir}/plugins/org.eclipse.gef*
%{eclipsedir}/plugins/org.eclipse.draw2d*
