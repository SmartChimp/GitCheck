import sublime
import sublime_plugin
import os

GIT_BASE_MASTER_BRANCH_URL = "https://github.com/freshdesk/helpkit/tree/rails3-phase2/"
GIT_BASE_STAGING_BRANCH_URL = "https://github.com/freshdesk/helpkit/tree/staging/"

class LookAtMasterCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		Utils.open_on_git(self.view, GIT_BASE_MASTER_BRANCH_URL)

class LookAtStagingCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		Utils.open_on_git(self.view, GIT_BASE_STAGING_BRANCH_URL)	

class Utils:

	@staticmethod
	def open_on_git(from_view, branch_url):
		splitted_path = from_view.file_name().split("/helpkit/")
		if(len(splitted_path) == 2):
			(row,col) = from_view.rowcol(from_view.sel()[0].begin())
			os.system('open '+branch_url+splitted_path[1]+"#L"+str(row+1))