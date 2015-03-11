---
layout: post
title: Vim improvements
---
These are things I think Vim needs improving on. Maybe I'll fix them some day.

- Faster regex matching

- A latex IDE that is minimal (doesn't clutter your maps) but provides solid functionality for compiling, viewing, indentation and error parsing. I have a set up that nearly does this. But there is a very ubtle bug in http://www.vim.org/scripts/script.php?script_id=2325 related to how it finds filenames. Need to remember what this is and fix it.

- The auto indent paste hack sometimes chops off the first few characters sometimes. This is the hack, put this in your `.vimrc`:

{% highlight vim %}
inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()
function! XTermPasteBegin()
  set pastetoggle=<Esc>[201~
  set paste
  return ""
endfunction
let &t_SI .= "\<Esc>[?2004h"
let &t_EI .= "\<Esc>[?2004l"
{% endhighlight %}

- Ability to use the repeat number feature for both inline operations and multiline operations. E.g. typing `2>>` indents two lines by one indent to the left. There should be an option like `-2>>` to indent one line twice.

- Case insensitivity for filename completion, e.g. `:e filename`.

- Not requiring a space prepending a string which you want to filename complete (`^X^F`)

- I don't understand why I should have to put `nnoremap cw dwi` in my `.vimrc`

- The repeat operation applied to `J` in normal mode applies one less repeat than I expect

- When opening giant files, the numbering pane on the left is set to the maximum size of the largest line no. This could be made be more efficient.

- Create a plugin that adds shortcuts for mathematical manipulations more easily. E.g. `Ctrl-A` adds to the next number (unless a minus sign precedes it). More shortcuts could be added to subtract and add regardless of a preceding minus sign. Also, float support would be good, but complex.
