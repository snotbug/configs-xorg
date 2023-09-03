local options = {
    number = true,
    relativenumber = true,
    signcolumn = "yes",
    cursorline = true,
    numberwidth = 4,
    showtabline = 4,
    linebreak = false,
    pumheight = 10,
    completeopt = { "menuone", "noselect" },
    termguicolors = true,
    cmdheight = 1,
    showmode = true,
    showcmd = false,

    tabstop = 4,
    softtabstop = 4,
    expandtab = true,
    shiftwidth = 4,
    smartindent = false,
    wrap = false,
    scrolloff = 8,
    sidescrolloff = 8,
    hlsearch = true,
    incsearch = true,
    smartcase = true,

    swapfile = false,
    backup = false,
    undofile = true,
    writebackup = false,
    fileencoding = "utf-8",

    mouse = "a",
    timeoutlen = 300,
    updatetime = 300,
}

for k, v in pairs(options) do
    vim.opt[k] = v
end

vim.opt.shortmess:append "c"
vim.opt.iskeyword:append "-"
vim.opt.formatoptions:remove({ "c", "r", "o" })
vim.opt.runtimepath:remove("/usr/share/vim/vimfiles")
