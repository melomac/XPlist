# XPlist

[Python](http://python.org/) command line tool.

Parse remote and local XProtect configuration files then print some stats.

### Example

	$ ./XPlist.py 
	Snow Leopard
	http://configuration.apple.com/configurations/macosx/xprotect/1/clientConfiguration.plist
	OSX.Abk                 1    A                                            
	OSX.RSPlug              3    A                                            
	OSX.Iservice            2    A, B                                         
	OSX.HellRTS             5                                                 
	OSX.OpinionSpy          1                                                 
	OSX.MacDefender        35    A, B, CDE, F, G, HI, J, K, L, M, N, O        
	OSX.QHost.WB            2    A                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.FlashBack          24    A, B, C                                      
	OSX.DevilRobber         5    A, B                                         
	OSX.FileSteal           2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.FkCodec             2    i                                            
	OSX.MaControl           1    i                                            
	OSX.SMSSend             2    i, ii                                        
	OSX.eicar.com           1    i                                            
	OSX.AdPlugin            1    i                                            
	OSX.AdPlugin2           1    i                                            
	OSX.Leverage            1    a                                            
	19 threats, 38 variants, 94 signatures (version 70).

	Lion
	http://configuration.apple.com/configurations/macosx/xprotect/2/clientConfiguration.plist
	OSX.Abk                 1    A                                            
	OSX.CoinThief           3    A, B                                         
	OSX.RSPlug              3    A                                            
	OSX.Iservice            2    A, B                                         
	OSX.HellRTS             5                                                 
	OSX.OpinionSpy          1                                                 
	OSX.MacDefender        14    A, B                                         
	OSX.QHost.WB            2    A                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.FlashBack          24    A, B, C                                      
	OSX.DevilRobber         5    A, B                                         
	OSX.FileSteal           2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.FkCodec             2    i                                            
	OSX.MaControl           1    i                                            
	OSX.SMSSend             2    i, ii                                        
	OSX.eicar.com           1    i                                            
	OSX.AdPlugin            1    i                                            
	OSX.AdPlugin2           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.Prxl                4    2                                            
	21 threats, 31 variants, 80 signatures (version 1055).

	Mountain Lion
	http://configuration.apple.com/configurations/macosx/xprotect/3/clientConfiguration.plist
	OSX.Abk                 1    A                                            
	OSX.CoinThief           3    A, B                                         
	OSX.RSPlug              3    A                                            
	OSX.Iservice            2    A, B                                         
	OSX.HellRTS             5                                                 
	OSX.OpinionSpy          1                                                 
	OSX.MacDefender        14    A, B                                         
	OSX.QHost.WB            2    A                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.FlashBack          22    A, B, C                                      
	OSX.DevilRobber         5    A, B                                         
	OSX.FileSteal           2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.FkCodec             2    i                                            
	OSX.MaControl           1    i                                            
	OSX.SMSSend             2    i, ii                                        
	OSX.eicar.com           1    i                                            
	OSX.AdPlugin            1    i                                            
	OSX.AdPlugin2           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.Prxl                3    2                                            
	21 threats, 31 variants, 77 signatures (version 2045).

	Mavericks
	http://swscan.apple.com/content/catalogs/others/index-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
	http://swcdn.apple.com/content/downloads/22/14/031-3414/a2lc4xs5wlvwg6axdcy12vfakmf9cu4vrs/XProtectPlistConfigData.pkg
	OSX.Abk                 1    A                                            
	OSX.CoinThief           3    A, B                                         
	OSX.RSPlug              3    A                                            
	OSX.Iservice            2    A, B                                         
	OSX.HellRTS             5                                                 
	OSX.OpinionSpy          1                                                 
	OSX.MacDefender        14    A, B                                         
	OSX.QHost.WB            2    A                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.FlashBack          22    A, B, C                                      
	OSX.DevilRobber         5    A, B                                         
	OSX.FileSteal           2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.FkCodec             2    i                                            
	OSX.MaControl           1    i                                            
	OSX.SMSSend             2    i, ii                                        
	OSX.eicar.com           1    i                                            
	OSX.AdPlugin            1    i                                            
	OSX.AdPlugin2           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.Prxl                3    2                                            
	21 threats, 31 variants, 77 signatures (version 2045).

	Local
	/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.plist
	/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist
	OSX.RSPlug              3    A                                            
	OSX.Iservice            2    A, B                                         
	OSX.HellRTS             5                                                 
	OSX.OpinionSpy          1                                                 
	OSX.MacDefender        14    A, B                                         
	OSX.QHost.WB            2    A                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.FlashBack          22    A, B, C                                      
	OSX.DevilRobber         5    A, B                                         
	OSX.FileSteal           2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.FkCodec             2    i                                            
	OSX.MaControl           1    i                                            
	OSX.SMSSend             2    i, ii                                        
	OSX.eicar.com           1    i                                            
	OSX.AdPlugin            1    i                                            
	OSX.AdPlugin2           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.Prxl                3    2                                            
	19 threats, 28 variants, 73 signatures (version 2044).
