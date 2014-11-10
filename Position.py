import sublime_plugin

##
# SublimePosition
#
# Shows current selection(s) position on Sublime Text status bar.
#
class Position(sublime_plugin.EventListener):

  def display_position(self, view):
    regions = (
      '-'.join(
        set([str(region.begin()), str(region.end())])
      ) for region in view.sel()
    )

    view.set_status('position', 'Position: ' + ', '.join(regions))

  def on_activated(self, view):
    self.display_position(view)

  def on_selection_modified(self, view):
    self.display_position(view)
