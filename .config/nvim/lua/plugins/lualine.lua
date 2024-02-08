-- Bubbles config for lualine
-- Author: lokesh-krishna
-- MIT license, see LICENSE for more details.

-- require('lualine').setup({
--   options = {
--     theme = 'auto',
--     component_separators = '|',
--     section_separators = { left = '', right = '' },
--   },
-- options = {
--   section_separators = { left = '', right = '' },
--   component_separators = { left = '', right = '' }
-- }
-- })

return {
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    opts = function()
      return {
        options = {
          section_separators = { left = '', right = '' },
          component_separators = '|'
        },
      }
    end,
  }
}
