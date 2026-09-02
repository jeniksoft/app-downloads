# Aplikace

Každá aplikace má vlastní složku:

```text
apps/<app-id>/
```

Složka aplikace obsahuje veřejný setup nebo SDK balík, popis, návod k použití a případné poznámky k verzi. Produktové zdrojové kódy ani LLM/model weights sem nepatří; výjimkou mohou být explicitně označené ukázkové zdroje uvnitř SDK balíku.

## Ke Stažení

| Aplikace | Verze | Setup / Balík | Dokumentace | SHA-256 |
| --- | --- | --- | --- | --- |
| Codex VeraCrypt Startup Mount | 1.0.187 | [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe) | [Popis a návod](veracrypt-startup-mount/README.md) | [`28AE4A59...C969D375`](../checksums/SHA256SUMS.txt) |
| Strategic Nexus Companion | 0.16.0 | [StrategicNexusCompanionSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/strategic-nexus-companion/StrategicNexusCompanionSetup.exe) | [Popis a návod](strategic-nexus-companion/README.md) | [`5AC5E5AB...239C8EB0`](../checksums/SHA256SUMS.txt) |
| Windows Update Restart Guard | 1.0.143 | [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe) | [Popis a návod](windows-update-restart-guard/README.md) | [`21EB9734...3C2DAF4C`](../checksums/SHA256SUMS.txt) |
| WDUi Framework SDK | 0.1.15 | [WduiFrameworkSdk-0.1.15.zip](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-framework/WduiFrameworkSdk-0.1.15.zip) | [Popis a návod](wdui-framework/README.md) | [`E3B5F881...760AE888`](../checksums/SHA256SUMS.txt) |
| WDUi Durable App Template | 1.0.41 | [WduiDurableAppTemplateSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-durable-app-template/WduiDurableAppTemplateSetup.exe) | [Popis a návod](wdui-durable-app-template/README.md) | [`D984C1C7...C472988C`](../checksums/SHA256SUMS.txt) |

Tabulky zkracují SHA-256 kvůli čitelnosti. Plný hash je v app `update.json` a `checksums/SHA256SUMS.txt`.

## Ve Vývoji

`Jarvis` je interní codename připravovaného projektu, nikoli finální produktový název. Cílem je bezplatná verze **Personal 1.0.0**, která bude zveřejněna pod jiným názvem. Aktuální stav je na stránce [Project codename: Jarvis](jarvis/README.md).

`Planetopia` je interní označení nové verze pluginu ve vývoji pro Unreal Engine 5.8. Aktuální veřejný report s českou částí a anglickým fallbackem je na stránce [Planetopia – vývojový report](planetopia/README.md). Nejde o veřejný download ani o prohlášení, že je produkt hotový.
