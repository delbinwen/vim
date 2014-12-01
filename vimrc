execute pathogen#infect('stuff/{}')
execute pathogen#helptags()
syntax on
filetype plugin indent on

" vim-airline configuration-------------------------------------------------
set laststatus=2
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1

" syntastic configuration----------------------------------------------------
" show list of errors and warnings on the current file
nmap <leader>e :Errors<CR>
" check also when just opened the file
let g:syntastic_check_on_open = 1
" don't put icons on the sign column (it hides the vcs status icons of
" signify)
let g:syntastic_enable_signs = 0
" custom icons (enable them if you use a patched font, and enable the
" previous setting)
let g:syntastic_error_symbol = '✗'
let g:syntastic_warning_symbol = '⚠'
let g:syntastic_style_error_symbol = '✗'
let g:syntastic_style_warning_symbol = '⚠'

" python-mode configuration--------------------------------------------------
" don't use linter, we use syntastic for that
let g:pymode_lint_on_write = 0
let g:pymode_lint_signs = 0
