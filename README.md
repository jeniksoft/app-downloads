# Jeniksoft App Downloads

Veřejné místo ke stažení vybraných Windows aplikací a utilit od Jeniksoft.

Toto repo je určené pro hotové instalační balíčky, popis aplikací, uživatelskou dokumentaci a kontrolní součty. Neobsahuje zdrojové kódy.

## Ke Stažení

| Aplikace | Verze | Setup | Dokumentace | SHA-256 |
| --- | --- | --- | --- | --- |
| Windows Update Restart Guard | 1.0.8 | [WindowsUpdateRestartGuardSetup.exe](apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe) | [Popis a návod](apps/windows-update-restart-guard/README.md) | `15B4E49CEF9B6B45EDA320A389C1643283C7E7BE033809AA5F00AA671EE4FE83` |

## Instalace

1. Otevři složku aplikace v tabulce výše.
2. Stáhni soubor `*Setup.exe`.
3. Spusť setup ve Windows.
4. Aplikaci můžeš později odebrat přes Windows Nastavení > Aplikace > Nainstalované aplikace.

## Bezpečnost A Důvěryhodnost

Instalátory jsou běžné Windows EXE soubory. Pokud ještě nejsou podepsané certifikátem s reputací, Windows SmartScreen nebo antivirus můžou zobrazit varování. Pro kontrolu integrity porovnej SHA-256 se souborem [checksums/SHA256SUMS.txt](checksums/SHA256SUMS.txt).

## Co Sem Patří

Do repa patří:

* `*Setup.exe` pro veřejné stažení
* krátký popis aplikace
* uživatelská dokumentace
* changelog nebo poznámky k verzi
* SHA-256 kontrolní součty

Do repa nepatří:

* zdrojové kódy
* privátní pracovní poznámky
* lokální konfigurace
* debug buildy a mezivýstupy
* interní skripty, které nejsou potřebné pro uživatele

## Struktura

```text
apps/
  <app-id>/
    README.md
    <AppName>Setup.exe
checksums/
  SHA256SUMS.txt
```
