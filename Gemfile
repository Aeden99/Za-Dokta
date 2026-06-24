source "https://rubygems.org"

# The github-pages gem pins Jekyll + all plugins to exactly what GitHub Pages
# runs, so "builds on my machine" == "builds on GitHub". This is what makes the
# zero-config "Deploy from a branch" path reliable.
gem "github-pages", group: :jekyll_plugins

# Needed for `jekyll serve` on Ruby 3.0+ (webrick left the standard library).
gem "webrick", "~> 1.8"

# Lock platform-specific gems so bundle install is reproducible across machines.
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
