
%define plugin	skinsoppalusikka
%define name	vdr-plugin-%plugin
%define version	1.6.5
%define rel	2

Summary:	VDR plugin: Soppalusikka skin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/
Source:		vdr-%plugin-%version.tgz
Obsoletes:	vdr-skin-soppalusikka < 1.6.0
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The "Soppalusikka" is a standalone skin providing the good old
"ElchiAIO" looks.

%vdr_chanlogo_notice

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Channel logo directory
var=LOGO_DIR
param=--logodir=LOGO_DIR
default=%{_vdr_chanlogodir}
%vdr_plugin_params_end

cat > README.install.urpmi <<EOF
%vdr_chanlogo_notice
EOF

%build
%vdr_plugin_build STRIP=/bin/true

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_themedir}
install -m644 themes/*.theme %{buildroot}%{_vdr_themedir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY README.install.urpmi
%{_vdr_themedir}/*.theme


%changelog
* Tue Jul 20 2010 Anssi Hannula <anssi@mandriva.org> 1.6.5-1mdv2011.0
+ Revision: 555058
- new version

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.6.4-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 1.6.4-1mdv2010.0
+ Revision: 396051
- new version
- update license tag
- drop COPYING, package is under GPL

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-3mdv2009.1
+ Revision: 359366
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-2mdv2009.0
+ Revision: 197978
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 197723
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- drop old provides
- versionize obsoletes
- update description

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 1.0.6-1mdv2008.1
+ Revision: 176922
- new version
- use upstream tarball, channel logos have been removed

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.0.4-6mdv2008.1
+ Revision: 145202
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.0.4-5mdv2008.1
+ Revision: 103212
- rebuild for new vdr
- fix description
- do not strip in %%build

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.0.4-4mdv2008.0
+ Revision: 50046
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.0.4-3mdv2008.0
+ Revision: 42129
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.0.4-2mdv2008.0
+ Revision: 22689
- rebuild for new vdr

* Tue Apr 24 2007 Anssi Hannula <anssi@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 17991
- 1.0.4


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.2-2mdv2007.0
+ Revision: 90971
- rebuild for new vdr

* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 1.0.2-1mdv2007.1
+ Revision: 76327
- 1.0.2

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-7mdv2007.1
+ Revision: 74082
- rebuild for new vdr
- Import vdr-plugin-skinsoppalusikka

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-5mdv2007.0
- stricter abi requires
- rename to vdr-plugin-skinsoppalusikka

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-2mdv2007.0
- use _ prefix for system path macros

* Fri Jun 16 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2007.0
- 1.0.1

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-2mdv2007.0
- rebuild for new vdr

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-1mdv2007.0
- initial Mandriva release

