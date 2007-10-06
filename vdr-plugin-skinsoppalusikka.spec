
%define plugin	skinsoppalusikka
%define name	vdr-plugin-%plugin
%define version	1.0.4
%define rel	4

Summary:	VDR plugin: Soppalusikka skin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/
# Channel logos are removed from the tarball
# gunzip vdr-skinsoppalusikka-*.tgz
# tar --wildcards --delete -f vdr-skinsoppalusikka-*.tar 'skinsoppalusikka-*/logos*'
# bzip2 vdr-skinsoppalusikka-*.tar
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
Obsoletes:	vdr-skin-soppalusikka
Provides:	vdr-skin-soppalusikka
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
The "Soppalusikka" is a standalone VDR skin based on "enElchi"
text2skin addon.

%vdr_chanlogo_notice

%prep
%setup -q -n %plugin-%version

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
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_themedir}
install -m644 themes/*.theme %{buildroot}%{_vdr_themedir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY README.install.urpmi
%{_vdr_themedir}/*.theme
