## Refelx / Dokku / GH Actions

Template Application.

Before deploying (your commit with gh actions), make sure you 

- Change the host and ssh key values in gh secrets
- Install dokku in the server and set it up [(see here)](https://dokku.com/docs/getting-started/installation/).
    
    ```bash
    # As of 16/11/2025
    # ----

    sudo apt update && sudo apt upgrade

    wget -NP . https://dokku.com/install/v0.36.10/bootstrap.sh
    sudo DOKKU_TAG=v0.36.10 bash bootstrap.sh

    cat ~/.ssh/authorized_keys | sudo dokku ssh-keys:add admin
    ```

    ```bash
    # you can use any domain you already have access to
    # this domain should have an A record or CNAME pointing at your server's IP
    dokku domains:set-global {your-domain-here-which-maps-to-ip}
    ```

    ```
    # SSL
    dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
    dokku letsencrypt:set --global email rozeappletree.dev@gmail.com
    dokku letsencrypt:cron-job --add
    ```