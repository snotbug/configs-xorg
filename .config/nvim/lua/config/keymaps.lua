local opts = { noremap = true, silent = true }
local term_opts = { silent = true }
local keymap = vim.api.nvim_set_keymap

keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- n: normal mode
-- i: insert mode
-- v: visual mode
-- x: visual block mode
-- t: term mode
-- c: command mode

-- navigate between windows
keymap("n", "<A-h>", "<C-w>h", opts)
keymap("n", "<A-j>", "<C-w>j", opts)
keymap("n", "<A-k>", "<C-w>k", opts)
keymap("n", "<A-l>", "<C-w>l", opts)

-- resize window size
keymap("n", "<C-Up>", ":resize -2<cr>", opts)
keymap("n", "<C-Down>", ":resize +2<cr>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<cr>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<cr>", opts)

-- move selected text vertically
keymap("v", "<S-j>", ":move '>+1<cr>gv-gv", opts)
keymap("v", "<S-k>", ":move '<-2<cr>gv-gv", opts)

-- navigate between buffers
keymap("n", "<S-l>", ":bnext<cr>", opts)
keymap("n", "<S-h>", ":bprevious<cr>", opts)

-- delete buffer
keymap("n", "<S-w>", "<cmd>bprevious<bar>bdelete#<cr>", opts)

-- clear highlights
keymap("n", "<leader>h", "<cmd>nohlsearch<cr>", opts)

-- copy selected text to global clipboard
keymap("v", "<leader>y", "\"+y", opts)
keymap("x", "<leader>y", "\"+y", opts)
keymap("n", "<leader>y", "\"+y", opts)

-- better paste
keymap("v", "p", '"_dP', opts)
keymap("x", "p", '"_dP', opts)

-- cursor remains same place
keymap("n", "J", "mzJ`z", opts)

keymap("n", "<C-u", "<C-u>zz", opts)
keymap("n", "<C-d>", "<C-d>zz", opts)

keymap("n", "n", "nzzzv", opts)
keymap("n", "N", "Nzzzv", opts)

keymap("n", "Q", "<nop>", opts)

-- stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- toggle nvim tree
keymap("n", "<leader>e", ":NvimTreeToggle<CR>", opts)

-- telescope
keymap("n", "<leader>ff", ":Telescope find_files<cr>", opts)
keymap("n", "<leader>ft", ":Telescope live_grep<cr>", opts)
keymap("n", "<leader>fb", ":Telescope buffers<cr>", opts)

-- lsp
keymap("n", "<leader>lf", "<cmd>lua vim.lsp.buf.format{ async = true }<cr>", opts)
