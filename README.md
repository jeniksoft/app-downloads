# Jeniksoft App Downloads

Veřejné místo ke stažení vybraných Windows aplikací a utilit od Jeniksoft.

Toto repo je určené pro hotové instalační balíčky, popis aplikací, uživatelskou dokumentaci a kontrolní součty. Neobsahuje zdrojové kódy ani LLM/model weights.

## Ke Stažení

| Aplikace | Verze | Setup | Dokumentace | SHA-256 |
| --- | --- | --- | --- | --- |
| VeraCrypt Startup Mount | 1.0.154 | [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe) | [Popis a návod](apps/veracrypt-startup-mount/README.md) | [`5E314DA7...CB8C3962`](checksums/SHA256SUMS.txt) |
| Jarvis | 0.1.313 | [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/jarvis/JarvisSetup.exe) | [Popis a návod](apps/jarvis/README.md) | [`00FE0E28...C7D1A6D1`](checksums/SHA256SUMS.txt) |
| Strategic Nexus Companion | 0.16.0 | [StrategicNexusCompanionSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/strategic-nexus-companion/StrategicNexusCompanionSetup.exe) | [Popis a návod](apps/strategic-nexus-companion/README.md) | [`5AC5E5AB...239C8EB0`](checksums/SHA256SUMS.txt) |
| Windows Update Restart Guard | 1.0.101 | [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe) | [Popis a návod](apps/windows-update-restart-guard/README.md) | [`8F322DBA...95553E82`](checksums/SHA256SUMS.txt) |

Setup odkazy v tabulce vedou přímo na GitHub raw download endpoint, aby kliknutí stáhlo instalační EXE místo otevření stránky binárního souboru.

Tabulky zkracují SHA-256 kvůli čitelnosti. Plný hash je vždy v `update.json` a [checksums/SHA256SUMS.txt](checksums/SHA256SUMS.txt).

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
* `history` - seznam verzí se změnami, aby aplikace při přeskočení verzí ukázala všechny relevantní změny od nainstalované verze

Volitelné pole `changes` může obsahovat obecný fallback text. Pole `history` používá objekty s `version`, `changes_cs`, `changes_en` a volitelným `changes`. Změny mají být krátké, uživatelské a vhodné pro zobrazení v tooltipu nebo update dialogu přímo v aplikaci; pokud uživatel přeskočí více verzí, aplikace má zobrazit kumulativní poznámky pro všechny novější verze.

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
* LLM/model weights nebo jiné velké modelové balíky
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
