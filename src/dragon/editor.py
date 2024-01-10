#!/usr/bin/env python3

# this file kind of sucks because i didn't really want to write it, honestly
# you (end user) are far better off learning to use the yaml format, its fairly simple to lay stuff
#   out yourself.
# but this also exists and should work good.

# if you're here to contribute to this file, im sorry. ::::)

import os, sys, pwd, pprint
import ruyaml as yaml
from .util import dprintline, OutputColors, OutputWeight

dbstate = lambda msg: dprintline(label_color=OutputColors.Green, tool_name="Project Editor",
                                 text_color=OutputColors.White, text_weight=OutputWeight.Bold, pusher=False, msg=msg)
dbwarn = lambda msg: dprintline(label_color=OutputColors.Yellow, tool_name="Project Editor",
                                text_color=OutputColors.White, text_weight=OutputWeight.Normal, pusher=False, msg=msg)
dberror = lambda msg: dprintline(label_color=OutputColors.Red, tool_name="Project Editor",
                                 text_color=OutputColors.White, text_weight=OutputWeight.Bold, pusher=False, msg=msg)


def get_input(prompt, default):
    dbstate(f'{prompt} ({default})')
    ret = input('>> ')
    return ret if ret.strip() else default


def get_from_selector(prompt, values, default):
    dbstate(prompt)
    itemlist = []
    for i, key in enumerate(values):
        print(f'[{i}] > {key}')
        itemlist.append(values[key])
    item = int(get_input('Select Item', default))
    return itemlist[item]


AppDelegate_h = """#import <UIKit/UIKit.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (nonatomic, strong) UIWindow *window;
@property (nonatomic, strong) UINavigationController *rootViewController;

@end
"""
AppDelegate_m = """#import "AppDelegate.h"
#import "RootViewController.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
	_window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
	_rootViewController = [[UINavigationController alloc] initWithRootViewController:[[RootViewController alloc] init]];
	_window.rootViewController = _rootViewController;
	[_window makeKeyAndVisible];
	return YES;
}

@end
"""
RootViewController_h = """#import <UIKit/UIKit.h>

@interface RootViewController : UITableViewController

@end
"""
RootViewController_m = """#import "RootViewController.h"

@interface RootViewController ()
@property (nonatomic, strong) NSMutableArray * objects;
@end

@implementation RootViewController

- (void)loadView {
	[super loadView];

	_objects = [NSMutableArray array];

	self.title = @"Root View Controller";
	self.navigationItem.leftBarButtonItem = self.editButtonItem;
	self.navigationItem.rightBarButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemAdd target:self action:@selector(addButtonTapped:)];
}

- (void)addButtonTapped:(id)sender {
	[_objects insertObject:[NSDate date] atIndex:0];
	[self.tableView insertRowsAtIndexPaths:@[ [NSIndexPath indexPathForRow:0 inSection:0] ] withRowAnimation:UITableViewRowAnimationAutomatic];
}

#pragma mark - Table View Data Source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
	return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
	return _objects.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
	static NSString *CellIdentifier = @"Cell";
	UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];

	if (!cell) {
		cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
	}

	NSDate *date = _objects[indexPath.row];
	cell.textLabel.text = date.description;
	return cell;
}

- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
	[_objects removeObjectAtIndex:indexPath.row];
	[tableView deleteRowsAtIndexPaths:@[ indexPath ] withRowAnimation:UITableViewRowAnimationAutomatic];
}

#pragma mark - Table View Delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
	[tableView deselectRowAtIndexPath:indexPath animated:YES];
}

@end
"""
main_m = """#import <Foundation/Foundation.h>
#import "AppDelegate.h"

int main(int argc, char *argv[]) {
	@autoreleasepool {
		return UIApplicationMain(argc, argv, nil, NSStringFromClass(AppDelegate.class));
	}
}
"""

InfoPlist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleExecutable</key>
	<string>bluh</string>
	<key>CFBundleIcons</key>
	<dict>
		<key>CFBundlePrimaryIcon</key>
		<dict>
			<key>CFBundleIconFiles</key>
			<array>
				<string>AppIcon29x29</string>
				<string>AppIcon40x40</string>
				<string>AppIcon57x57</string>
				<string>AppIcon60x60</string>
			</array>
			<key>UIPrerenderedIcon</key>
			<true/>
		</dict>
	</dict>
	<key>CFBundleIcons~ipad</key>
	<dict>
		<key>CFBundlePrimaryIcon</key>
		<dict>
			<key>CFBundleIconFiles</key>
			<array>
				<string>AppIcon29x29</string>
				<string>AppIcon40x40</string>
				<string>AppIcon57x57</string>
				<string>AppIcon60x60</string>
				<string>AppIcon50x50</string>
				<string>AppIcon72x72</string>
				<string>AppIcon76x76</string>
			</array>
			<key>UIPrerenderedIcon</key>
			<true/>
		</dict>
	</dict>
	<key>CFBundleIdentifier</key>
	<string>{}</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleSupportedPlatforms</key>
	<array>
		<string>iPhoneOS</string>
	</array>
	<key>CFBundleVersion</key>
	<string>1.0</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UIDeviceFamily</key>
	<array>
		<integer>1</integer>
		<integer>2</integer>
	</array>
	<key>UIRequiredDeviceCapabilities</key>
	<array>
		<string>armv7</string>
	</array>
	<key>UILaunchImageFile</key>
	<string>LaunchImage</string>
	<key>UILaunchImages</key>
	<array>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{{320, 480}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-700-568h</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{{320, 568}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-Portrait</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{{768, 1024}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-Landscape</string>
			<key>UILaunchImageOrientation</key>
			<string>Landscape</string>
			<key>UILaunchImageSize</key>
			<string>{{768, 1024}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>8.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-800-667h</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{{375, 667}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>8.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-800-Portrait-736h</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{{414, 736}}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>8.0</string>
			<key>UILaunchImageName</key>
			<string>LaunchImage-800-Landscape-736h</string>
			<key>UILaunchImageOrientation</key>
			<string>Landscape</string>
			<key>UILaunchImageSize</key>
			<string>{{414, 736}}</string>
		</dict>
	</array>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
</dict>
</plist>
"""

Prefs_LPLP_NamePlist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>entry</key>
	<dict>
		<key>bundle</key>
		<string>{}</string>
		<key>cell</key>
		<string>PSLinkCell</string>
		<key>detail</key>
		<string>{}RootListController</string>
		<key>icon</key>
		<string>icon.png</string>
		<key>isController</key>
		<true/>
		<key>label</key>
		<string>{}</string>
	</dict>
</dict>
</plist>"""

Prefs_R_InfoPlist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>English</string>
	<key>CFBundleExecutable</key>
	<string>{}</string>
	<key>CFBundleIdentifier</key>
	<string>{}</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundlePackageType</key>
	<string>BNDL</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0.0</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleVersion</key>
	<string>1.0</string>
	<key>NSPrincipalClass</key>
	<string>{}RootListController</string>
</dict>
</plist>
"""

Prefs_R_RootPlist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>items</key>
	<array>
		<dict>
			<key>cell</key>
			<string>PSGroupCell</string>
			<key>label</key>
			<string>{} First Page</string>
		</dict>
		<dict>
			<key>cell</key>
			<string>PSSwitchCell</string>
			<key>default</key>
			<true/>
			<key>defaults</key>
			<string>{}</string>
			<key>key</key>
			<string>AwesomeSwitch1</string>
			<key>label</key>
			<string>Awesome Switch 1</string>
		</dict>
	</array>
	<key>title</key>
	<string>{}</string>
</dict>
</plist>
"""

Prefs_RootListController_h = """#import <Preferences/PSListController.h>

@interface {}RootListController : PSListController

@end
"""
Prefs_RootListController_m = """#import <Foundation/Foundation.h>
#import "{}RootListController.h"

@implementation {}RootListController

- (NSArray *)specifiers {{
	if (!_specifiers) {{
		_specifiers = [self loadSpecifiersFromPlistName:@"Root" target:self];
	}}

	return _specifiers;
}}

@end
"""


FWK_R_InfoPlist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>English</string>
	<key>CFBundleExecutable</key>
	<string>{}</string>
	<key>CFBundleIdentifier</key>
	<string>{}</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundlePackageType</key>
	<string>FMWK</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleVersion</key>
	<string>1</string>
</dict>
</plist>
"""

FWK_name_h = """// Umbrella header for {}.
// Add import lines for each public header, like this: #import <{}/XXXAwesomeClass.h>
// Don’t forget to also add them to {} in your Makefile!
"""


class Project:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.directory_name = self.root_directory.split('/')[-1]
        self.current_username = pwd.getpwuid(os.getuid()).pw_name
        self.variables = {}

    def create_new(self):
        dbstate('-=-=============================')
        dbstate('Creating new Package')
        dbstate('-=-=============================')
        self.variables['name'] = get_input('Project Name', self.directory_name)
        self.variables['id'] = get_input('Bundle ID', f'com.{self.current_username}.{self.directory_name}')
        self.variables['depends'] = 'mobilesubstrate'
        self.variables['architecture'] = 'iphoneos-arm'
        self.variables['version'] = get_input('Version', '0.0.1')
        self.variables['description'] = get_input('Description', 'A cool MobileSubstrate Tweak')
        self.variables['author'] = get_input('Author', self.current_username)
        self.variables['section'] = 'Tweaks'


class Module:
    def __init__(self, variables=None):
        if variables is None:
            variables = {}
        self.variables = {}
        if 'id' in variables:
            self.variables['id'] = variables['id']
        if 'author' in variables:
            self.variables['author'] = variables['author']
        self.name = ''

    def create_new(self, proj_root):
        dbstate('-=-=============================')
        dbstate('Creating new Module')
        dbstate('-=-=============================')
        self.variables['type'] = get_from_selector('Select Module Type', {'Tweak': 'tweak', 'App': 'app',
                                                                          'CLI Tool': 'cli', 'Library': 'library',
                                                                          'Preference Bundle': 'prefs',
                                                                          'Framework': 'framework',}, '0')
        self.name = get_input('Name', 'ModuleName')
        while True:
            subdir = get_input('Subdirectory Name (Leave empty to work in current directory)', '')
            if subdir != '':
                if os.path.exists(subdir):
                    print('File/Directory already exists;')
                    continue
                else:
                    self.variables['dir'] = subdir
                    os.mkdir(subdir)
                    break
            else:
                break
        self._new_for_type(self.variables['type'], proj_root)

    def _new_for_type(self, type, proj_root):
        if 'dir' in self.variables:
            os.chdir(self.variables['dir'])

        if type == 'tweak':
            self.variables['filter'] = {
                'executables': get_input('Comma separated list of processes to target', 'SpringBoard').split(', ')}
            self.variables['files'] = [f'{self.name}.x']
            with open(f'{self.name}.x', 'w') as out:
                out.write('// Insert your code here!\n')
        elif type == 'framework':
            if not os.path.exists('Resources'):
                os.mkdir('Resources')
            with open('Resources/Info.plist', 'w') as out:
                out.write(FWK_R_InfoPlist.format(self.name, self.variables['id']))
            with open(f'{self.name}.h', 'w') as out:
                out.write(FWK_name_h.format(self.name, self.name, self.name))
            with open(f'{self.name}.m', 'wb') as out:
                out.write(b'')
            self.variables['files'] = [f'{self.name}.m']
        elif type == 'library':
            with open(f'{self.name}.m', 'wb') as out:
                out.write(b'')
            self.variables['files'] = [f'{self.name}.m']
        elif type == 'prefs':
            self.variables['prefix'] = get_input('Class name prefix (three or more characters unique to this project)',
                                                 self.name)
            if not os.path.exists(proj_root + os.path.sep + 'layout'):
                os.mkdir(proj_root + os.path.sep + 'layout')
            if not os.path.exists(proj_root + os.path.sep + 'layout' + os.path.sep + 'Library'):
                os.mkdir(proj_root + os.path.sep + 'layout' + os.path.sep + 'Library')
            if not os.path.exists(
                    proj_root + os.path.sep + 'layout' + os.path.sep + 'Library' + os.path.sep + 'PreferenceLoader'):
                os.mkdir(
                    proj_root + os.path.sep + 'layout' + os.path.sep + 'Library' + os.path.sep + 'PreferenceLoader')
            if not os.path.exists(
                    proj_root + os.path.sep + 'layout' + os.path.sep + 'Library' + os.path.sep + 'PreferenceLoader' + os.path.sep + 'Preferences'):
                os.mkdir(
                    proj_root + os.path.sep + 'layout' + os.path.sep + 'Library' + os.path.sep + 'PreferenceLoader' + os.path.sep + 'Preferences')
            with open(
                    proj_root + os.path.sep + 'layout' + os.path.sep + 'Library' + os.path.sep + 'PreferenceLoader' + os.path.sep + 'Preferences' + os.path.sep + self.name + '.plist',
                    'w') as out:
                out.write(Prefs_LPLP_NamePlist.format(self.name, self.variables['prefix'], self.name))
            if not os.path.exists('Resources'):
                os.mkdir('Resources')
            with open('Resources/icon.png', 'wb') as out:
                out.write(b'')
            with open('Resources/icon@2x.png', 'wb') as out:
                out.write(b'')
            with open('Resources/icon@3x.png', 'wb') as out:
                out.write(b'')
            with open('Resources/Info.plist', 'w') as out:
                out.write(Prefs_R_InfoPlist.format(self.name, self.variables['id'], self.variables['prefix']))
            with open('Resources/Root.plist', 'w') as out:
                out.write(Prefs_R_RootPlist.format(self.name, self.variables['id'], self.name))
            self.variables['files'] = [self.variables['prefix'] + 'RootListController.m']
            with open(self.variables['prefix'] + 'RootListController.m', 'w') as out:
                out.write(Prefs_RootListController_m.format(self.variables['prefix'], self.variables['prefix']))
            with open(self.variables['prefix'] + 'RootListController.h', 'w') as out:
                out.write(Prefs_RootListController_h.format(self.variables['prefix']))
        elif type == 'app':
            self.variables['files'] = ['AppDelegate.m', 'RootViewController.m', 'main.m']
            with open('AppDelegate.h', 'w') as out:
                out.write(AppDelegate_h)
            with open('AppDelegate.m', 'w') as out:
                out.write(AppDelegate_m)
            with open('RootViewController.h', 'w') as out:
                out.write(RootViewController_h)
            with open('RootViewController.m', 'w') as out:
                out.write(RootViewController_m)
            with open('main.m', 'w') as out:
                out.write(main_m)
            os.mkdir('Resources')
            _l = 'AppIcon29x29.png AppIcon29x29@2x.png AppIcon29x29@3x.png AppIcon40x40.png AppIcon40x40@2x.png ' \
                 'AppIcon40x40@3x.png AppIcon50x50.png AppIcon50x50@2x.png AppIcon57x57.png AppIcon57x57@2x.png ' \
                 'AppIcon57x57@3x.png AppIcon60x60.png AppIcon60x60@2x.png AppIcon60x60@3x.png AppIcon72x72.png ' \
                 'AppIcon72x72@2x.png AppIcon76x76.png AppIcon76x76@2x.png LaunchImage-700-568h@2x.png ' \
                 'LaunchImage-700-Landscape@2x~ipad.png LaunchImage-700-Landscape~ipad.png ' \
                 'LaunchImage-700-Portrait@2x~ipad.png LaunchImage-700-Portrait~ipad.png LaunchImage-800-667h@2x.png ' \
                 'LaunchImage-800-Landscape-736h@3x.png LaunchImage-800-Portrait-736h@3x.png LaunchImage.png ' \
                 'LaunchImage@2x.png'.split(' ')
            for file in _l:
                with open(f'Resources/{file}', 'wb') as out:
                    out.write(b'')
            with open(f'Resources/Info.plist', 'w') as out:
                out.write(InfoPlist.format(self.variables['id']))

        try:
            del self.variables['id']
        except Exception:
            pass
        try:
            del self.variables['author']
        except Exception:
            pass
        try:
            del self.variables['prefix']
        except Exception:
            pass


class ProjectEditor:
    def __init__(self):

        self.project_root_directory = os.getcwd()

        if os.path.exists('DragonMake'):
            with open('DragonMake') as f:
                self.config = yaml.safe_load(f)
                self.preexisting_config = True
        else:
            self.config = {}
            self.preexisting_config = False

        if self.config is None:  # ??
            self.config = {}
            self.preexisting_config = False

    def create_new_module(self) -> Module:
        if not self.preexisting_config:
            project = Project(self.project_root_directory)
            project.create_new()
            self.config = project.variables

        mod = Module(self.config)
        mod.create_new(self.project_root_directory)
        self.config[mod.name] = mod.variables
        os.chdir(self.project_root_directory)
        return mod


def main():
    editor = ProjectEditor()
    mod = editor.create_new_module()

    path = 'DragonMake'
    if 'dir' in mod.variables:
        path = mod.variables['dir'] + '/' + path

    with open(path, 'w') as f:
        f.write(yaml.dump(editor.config, Dumper=yaml.RoundTripDumper))


if __name__ == '__main__':
    main()
