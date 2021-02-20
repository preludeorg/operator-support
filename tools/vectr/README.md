# VECTR

VECTR is a purple team tool for manual security assessments (campaign planning & reporting). 

This repository contains a simple Vagrantfile to spin up a server with VECTR pre-installed. 

## Install 

```
vagrant up
```

### Debug notes

When you launch this image and navigate to https://localhost:8081, you may notice being redirected to https://sravectr.internal:8081/auth/login. You will need to replace this with https://localhost:8081.
