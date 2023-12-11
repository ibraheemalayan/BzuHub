# Project Development Setup

## Setup database on localhost

- Install **Postgresql DB Engine** >=12, [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- Install **PgAdmin** (optional if you want to use a GUI)
- Create a new user

  - (in the PgAdmin called Create Role) named `bhuser`
  - with password `438e9whfewAL7L4JADSoR84` ( in PgAdmin set the password in the `Definition` tab )
  - with privilages 1. `Can login?` 3. `Create DB?`

  ```SQL
  CREATE ROLE bhuser WITH
  LOGIN
  NOSUPERUSER
  CREATEDB
  NOCREATEROLE
  INHERIT
  NOREPLICATION
  CONNECTION LIMIT -1
  PASSWORD '438e9whfewAL7L4JADSoR84';
  ```

- Create a new database named `bzuhubdb` and set its owner to `bhuser`

  ```SQL
  CREATE DATABASE bzuhubdb
    WITH
    OWNER = bhuser
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
  ```

## Setup project on localhost

- Install **Python** >= 3.11
- Install **python pip**
- Add Python, scripts to PATH

  - Windows

    ```
     {Python_dir}\Python311\Scripts\
     {Python_dir}\Python311\
    ```

  - Unix ( mac / linux )

    ```
    No need to add anything
    ```

- Clone Repository

  ```zsh
  git clone https://github.com/ibraheemalayan/BzuHub.git
  ```

  ```zsh
  cd BzuHub
  ```

- Bzuhub Python Venv

  - Windows

    ```
    not tested yet (you can skip this, although not recommended, or try it yourself)
    ```

  - Unix ( mac / linux )

    - in bzuhub_home directory run:

    ```
    python3 -m venv bzuhub_venv
    ```

- install required modules

  > **FOR MAC OS** install the Postgres App then run this command before installing requirements
  >
  > ```zsh
  > export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
  > ```

  ```zsh
  source bzuhub_venv/bin/activate
  pip3 install -r requirements.txt
  ```

  > do not forget to activate the venv ( select its interpreter ) in your IDE ( in vscode `Ctrl + P` then `Python: Select Interpreter` )

  ```zsh
  cd src
  ```

- redirect domains to 127.0.0.1

  - Windows

    - open a powershell console as administrator and run:

      ```powershell
      Add-Content -Path 'C:\Windows\System32\drivers\etc\hosts' -Value '127.0.0.1     www.dev-bzuhub.com'
      ```

    - clear dns cache
      ```powershell
      ipconfig /flushdns
      ```

  - Mac OS (unix)

    > Note: if lookups against hosts file are slow, [see this answer](https://superuser.com/questions/1596225/dns-resolution-delay-for-entries-in-etc-hosts#)

    - open a terminal run:

      ```zsh
      sudo zsh -c "echo -e '::1\twww.dev-bzuhub.com' >> /etc/hosts"
      ```

    - clear dns cache
      ```zsh
      sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
      ```

  - Linux

    - open a terminal run:

      ```zsh
      sudo su
      echo -e '127.0.0.1\twww.dev-bzuhub.com' >> /etc/hosts
      ```

    - no need to flush DNS
