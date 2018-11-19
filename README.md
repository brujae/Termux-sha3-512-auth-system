<h1 align="center">
  <br>
  Advanced login system for termux using sha3-512
  <br>
</h1>

1 Line quick install: `git clone https://github.com/DecodeMehh/termux-login-system-sha3-512 && cd termux-login-system-sha3-512 && mv auth.py $HOME/auth.py && rm -rf $HOME/termux-login-system-sha3-512 && cd $HOME/../usr/etc && echo "python auth.py" >> bash.bashrc && cd $HOME && clear && echo "install done :)!"`

* Default Username: `73214`
* Default Password: `1337`

<h2>How to edit password and username?</h2>

Open your browser and go to <a href="https://duckduckgo.com">DuckDuckGo</a> and type `sha3-512 Yourstring` and as duckduckgo are smart they will answer you with the hash
then do `cd $HOME && nano auth.py` there you will see the source code you only gotta add your hashed string into `sha3_512uname = "yourstring goes here"` and `sha3_512pword` for the password.

Using `echo yourstring | sha3 -a 512` don't work i realy don't know why 🤔

<h2>Requirements:</h2>
<a href="https://github.com/dylanaraps/neofetch">NeoFetch</a>

And maybe some other...
