require("config.lazy")
require("lazy").setup("plugins")
require("config.vim-options")
require("plugins.lsp-config")
vim.cmd [[
  highlight Normal guibg=none
  highlight NonText guibg=none
  highlight Normal ctermbg=none
  highlight NonText ctermbg=none
]]
vim.opt.clipboard = "unnamedplus"
