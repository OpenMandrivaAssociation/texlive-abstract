Name:		texlive-abstract
Version:	1.2a
Release:	1
Summary:	Control the typesetting of the abstract environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abstract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The abstract package gives you control over the typesetting of
the abstract environment, and in particular provides for a one
column abstract in a two column paper.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
