//
//  ViewController.m
//  BuildPackage-Example
//
//  Created by xiaochenghua on 2019/7/31.
//  Copyright © 2019 xiaochenghua. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    UILabel *versionLabel = [[UILabel alloc] init];
    versionLabel.font = [UIFont systemFontOfSize:20.0f];
    versionLabel.textColor = UIColor.whiteColor;
    versionLabel.backgroundColor = UIColor.grayColor;
    versionLabel.text = [NSString stringWithFormat:@"版本号: %@", [self getAppVersion]];
    
    [self.view addSubview:versionLabel];
    
    [versionLabel mas_makeConstraints:^(MASConstraintMaker *make) {
        make.center.equalTo(self.view);
    }];
}

- (NSString *)getAppVersion {
    NSString *version = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleShortVersionString"];
    NSString *build = [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleVersion"];
    return [NSString stringWithFormat:@"%@-%@", version, build];
}


@end
