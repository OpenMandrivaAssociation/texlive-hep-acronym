Name:		texlive-hep-acronym
Version:	64890
Release:	2
Summary:	An acronym extension for glossaries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-acronym
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-acronym package provides an acronym macro based on the
glossaries package. The package is loaded with
\usepackage{hep-acronym}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-acronym
%{_texmfdistdir}/tex/latex/hep-acronym
%doc %{_texmfdistdir}/doc/latex/hep-acronym

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
