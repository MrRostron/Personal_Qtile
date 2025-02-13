return {
	"MeanderingProgrammer/dashboard.nvim",
	event = "VimEnter",
	dependencies = {
		{ "MaximilianLloyd/ascii.nvim", dependencies = { "MunifTanjim/nui.nvim" } },
	},
	config = function()
		require("dashboard").setup({
			header = require("ascii").art.text.neovim.sharp,
			directories = {
				"~/.config",
				"~/.config/qtile",
				"~/.config/nvim",
				"~/cs50",
				"~/MacTrickz",
				"~/sock",
			},
		})
	end,
}
