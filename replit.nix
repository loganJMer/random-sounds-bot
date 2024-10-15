{ pkgs }: {
  deps = [
    pkgs.python311Packages.flask
    pkgs.python310Packages.flask
    pkgs.libopus
    pkgs.ffmpeg
  ];
  env = {
  };
}