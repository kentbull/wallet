# Wallet

RootGAR Software

### Poetry set up

`make setup`

### Developing

`poetry shell`

`export WALLET_ENVIRONMENT=development; poetry run flet main.py` or `make dev`

#### Code style and formatting

See editor integration: https://docs.astral.sh/ruff/editors/setup/ or `make fmt`

#### Local services

Running locally is intended to work with the sample set of six witnesses provided by the `kli witness demo` command.

Run the following two services prior to running Wallet, the witness pool and the vLEI server:

```bash
# In one terminal window run 
kli witness demo

# and in another terminal window run
vLEI-server -s ./schema/acdc -c ./samples/acdc/ -o ./samples/oobis/
```

### Other environments

Wallet allows configuration of the witnesses used, agent configuration directory, and inception
configuration file with the following environment variables. You can also specify only
WALLET_ENVIRONMENT and the other  variables will all be set to valid values.

### Environment Toggle
- `WALLET_ENVIRONMENT`: production, staging, or development

#### Changing the environment for a deployed Wallet app bundle

To change the environment of a deployed Wallet app bundle add the following LSEnvironment key and the corresponding dict of environment variables to the `wallet.app/Contents/Info.plist` file:
```xml
<plist>
  ...
  <key>LSEnvironment</key>
  <dict>
    <key>WALLET_ENVIRONMENT</key>
    <string>development</string>
  </dict>
  ...
</plist>
```

### Configuration Overrides

- `WITNESS_POOL_PATH`: Path to a JSON file containing key value pairs where the key is the
  pool name and the value is an array of witnesses.
- `KERI_CONFIG_DIR`: Path to a directory containing agent configuration including the
  bootstrap configuration file specified with the next environment variable.
- `KERI_AGENT_CONFIG_FILE`: The environment variable specifying the name only of the
  agent configuration file.

### Staging

You do not need to run witnesses or the vLEI server locally for testing with staging because they are already running. Set a few variables to point to staging and then run Wallet.

```bash
export WALLET_ENVIRONMENT=staging

poetry run python main.py
```

### Production

Since the default config uses production then you just run Wallet.

```bash
poetry run python main.py
```

Run the app normally. The default is to use the production


### Signing

See the process to add a keychain item for stored credentials useing app specific passwords https://developer.apple.com/documentation/security/customizing-the-notarization-workflow

Add a new keychain item for signing:

```
xcrun notarytool store-credentials "org.example.foo"
--apple-id "<AppleID>"
--team-id <DeveloperTeamID>
--password <secret_2FA_password>
```

Run sign.sh

```
export WALLET_ENVIRONMENT="development"; export DEVELOPER_ID_APP_CERT="Developer ID Application: YOUR_ID_HERE"; make sign
```

`DEVELOPER_ID_APP_CERT` can be found using `security find-identity -p basic`