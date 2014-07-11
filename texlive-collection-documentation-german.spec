# revision 25301
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-german
Epoch:		1
Version:	20120224
Release:	7
Summary:	German documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-german.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-einfuehrung
Requires:	texlive-fifinddo-info
Requires:	texlive-kopka
Requires:	texlive-l2picfaq
Requires:	texlive-l2tabu
Requires:	texlive-latex-bib-ex
Requires:	texlive-latex-referenz
Requires:	texlive-latex-tabellen
Requires:	texlive-lshort-german
Requires:	texlive-presentations
Requires:	texlive-pstricks-examples
Requires:	texlive-templates-fenn
Requires:	texlive-templates-sommer
Requires:	texlive-texlive-de
Requires:	texlive-translation-arsclassica-de
Requires:	texlive-translation-biblatex-de
Requires:	texlive-translation-chemsym-de
Requires:	texlive-translation-ecv-de
Requires:	texlive-translation-enumitem-de
Requires:	texlive-translation-europecv-de
Requires:	texlive-translation-filecontents-de
Requires:	texlive-translation-moreverb-de
Requires:	texlive-voss-de
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-german package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780216
- Update to latest release.
- Import texlive-collection-documentation-german
- Import texlive-collection-documentation-german

