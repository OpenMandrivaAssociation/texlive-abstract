Name:		texlive-abstract
Version:	15878
Release:	2
Summary:	Control the typesetting of the abstract environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abstract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The abstract package gives you control over the typesetting of
the abstract environment, and in particular provides for a one
column abstract in a two column paper.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/abstract/abstract.sty
%doc %{_texmfdistdir}/doc/latex/abstract/README
%doc %{_texmfdistdir}/doc/latex/abstract/abstract.pdf
#- source
%doc %{_texmfdistdir}/source/latex/abstract/abstract.dtx
%doc %{_texmfdistdir}/source/latex/abstract/abstract.ins

#-----------------------------------------------------------------------
%prep
%setup -q -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
