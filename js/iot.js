 function LigarIoT() {
    "use strict;"

    var exec = require('child_process').exec;
    const cmd = 'sudo ./start.sh';

    exec(cmd, {
      cwd: __dirname
      }, (err, stdout, stderr) => {
      console.log(stdout);
      if (err) console.log(err);
      else runCommand(cmds, cb);
    });
}

