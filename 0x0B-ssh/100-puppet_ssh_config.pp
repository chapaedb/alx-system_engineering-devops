# Using Puppet to make changes to the default SSH config file
# so that one can connect to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation
#
# ^        Beginning of the line
# [#]*     At least one hash character
# [\s]*    Zero or more whitespace characters
# (?i)     Case insensitive
# IdentityFile    Literal string "IdentityFile"
# [\s]+    At least one whitespace character
# ~/.ssh/id_rsa    The SSH private key file path we want to replace
# $        End of the line

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation
#
# ^        Beginning of the line
# [#]*     At least one hash character
# [\s]*    Zero or more whitespace characters
# (?i)     Case insensitive
# PasswordAuthentication    Literal string "PasswordAuthentication"
# [\s]+    At least one whitespace character
# (yes|no)    Match either "yes" or "no"
# $        End of the line
