%global tl_name hep-acronym
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	An acronym extension for glossaries
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-acronym
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-acronym.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hep-acronym package provides an acronym macro based on the
glossaries package. The package is loaded with \usepackage{hep-acronym}.

