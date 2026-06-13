# Jeniksoft App Downloads

Veřejné místo ke stažení vybraných Windows aplikací a utilit od Jeniksoft.

Toto repo je určené pro hotové instalační balíčky, popis aplikací, uživatelskou dokumentaci a kontrolní součty. Neobsahuje zdrojové kódy.

## Ke Stažení

| Aplikace | Verze | Setup | Dokumentace | SHA-256 |
| --- | --- | --- | --- | --- |
| Windows Update Restart Guard | 1.0.21 | [WindowsUpdateRestartGuardSetup.exe](apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe) | [Popis a návod](apps/windows-update-restart-guard/README.md) | `A91163241CA7942574ACB2AB0EF198242B1B6461956180C96031311F505B89B6` |

## Update Manifest

Každá aplikace, která umí kontrolu aktualizací přímo v aplikaci, musí mít ve své složce `update.json`. Manifest je veřejný kontrakt pro aplikaci i uživatele a musí popisovat přesně poslední publikovaný setup.

Povinná pole:

* `app_id` - stabilní identifikátor aplikace
* `name` - uživatelský název aplikace
* `version` - publikovaná verze setupu
* `release_url` - GitHub release nebo stránka verze
* `setup_url` - přímý odkaz na `*Setup.exe`
* `sha256` - SHA-256 publikovaného setupu
* `changes_cs` - stručně, co se v této verzi změnilo, česky
* `changes_en` - stručně, co se v této verzi změnilo, anglicky

Volitelné pole `changes` může obsahovat obecný fallback text. Změny mají být krátké, uživatelské a vhodné pro zobrazení v tooltipu nebo update dialogu přímo v aplikaci.

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
    update.json
    <AppName>Setup.exe
checksums/
  SHA256SUMS.txt
```
