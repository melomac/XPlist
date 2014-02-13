# XPlist

[Python](http://python.org/) command line tool.

Parse remote and local XProtect configuration files then print some stats.

### Example

	$ ./XPlist.py 
	Snow Leopard
	http://configuration.apple.com/configurations/macosx/xprotect/1/clientConfiguration.plist
	OSX.SMSSend             2    i, ii                                        
	OSX.HellRTS             5                                                 
	OSX.FkCodec             2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.RSPlug              3    A                                            
	OSX.MaControl           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.MacDefender        35    A, B, CDE, F, G, HI, J, K, L, M, N, O        
	OSX.AdPlugin2           1    i                                            
	OSX.FileSteal           2    i                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.eicar.com           1    i                                            
	OSX.Iservice            2    A, B                                         
	OSX.FlashBack          24    A, B, C                                      
	OSX.Abk                 1    A                                            
	OSX.AdPlugin            1    i                                            
	OSX.QHost.WB            2    A                                            
	OSX.DevilRobber         5    A, B                                         
	OSX.OpinionSpy          1                                                 
	19 threats, 38 variants, 94 signatures (version 70).

	Lion
	http://configuration.apple.com/configurations/macosx/xprotect/2/clientConfiguration.plist
	OSX.SMSSend             2    i, ii                                        
	OSX.HellRTS             5                                                 
	OSX.FkCodec             2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.Prxl                4    2                                            
	OSX.RSPlug              3    A                                            
	OSX.MaControl           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.MacDefender        14    A, B                                         
	OSX.CoinThief           3    A, B                                         
	OSX.AdPlugin2           1    i                                            
	OSX.FileSteal           2    i                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.eicar.com           1    i                                            
	OSX.Iservice            2    A, B                                         
	OSX.FlashBack          24    A, B, C                                      
	OSX.Abk                 1    A                                            
	OSX.AdPlugin            1    i                                            
	OSX.QHost.WB            2    A                                            
	OSX.DevilRobber         5    A, B                                         
	OSX.OpinionSpy          1                                                 
	21 threats, 31 variants, 80 signatures (version 1055).

	Mountain Lion
	http://configuration.apple.com/configurations/macosx/xprotect/3/clientConfiguration.plist
	OSX.SMSSend             2    i, ii                                        
	OSX.HellRTS             5                                                 
	OSX.FkCodec             2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.Prxl                3    2                                            
	OSX.RSPlug              3    A                                            
	OSX.MaControl           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.MacDefender        14    A, B                                         
	OSX.CoinThief           3    A, B                                         
	OSX.AdPlugin2           1    i                                            
	OSX.FileSteal           2    i                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.eicar.com           1    i                                            
	OSX.Iservice            2    A, B                                         
	OSX.FlashBack          22    A, B, C                                      
	OSX.Abk                 1    A                                            
	OSX.AdPlugin            1    i                                            
	OSX.QHost.WB            2    A                                            
	OSX.DevilRobber         5    A, B                                         
	OSX.OpinionSpy          1                                                 
	21 threats, 31 variants, 77 signatures (version 2045).

	Mavericks
	http://swscan.apple.com/content/catalogs/others/index-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
	http://swcdn.apple.com/content/downloads/22/14/031-3414/a2lc4xs5wlvwg6axdcy12vfakmf9cu4vrs/XProtectPlistConfigData.pkg
	OSX.SMSSend             2    i, ii                                        
	OSX.HellRTS             5                                                 
	OSX.FkCodec             2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.Prxl                3    2                                            
	OSX.RSPlug              3    A                                            
	OSX.MaControl           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.MacDefender        14    A, B                                         
	OSX.CoinThief           3    A, B                                         
	OSX.AdPlugin2           1    i                                            
	OSX.FileSteal           2    i                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.eicar.com           1    i                                            
	OSX.Iservice            2    A, B                                         
	OSX.FlashBack          22    A, B, C                                      
	OSX.Abk                 1    A                                            
	OSX.AdPlugin            1    i                                            
	OSX.QHost.WB            2    A                                            
	OSX.DevilRobber         5    A, B                                         
	OSX.OpinionSpy          1                                                 
	21 threats, 31 variants, 77 signatures (version 2045).

	Local
	/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.plist
	/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist
	OSX.SMSSend             2    i, ii                                        
	OSX.HellRTS             5                                                 
	OSX.FkCodec             2    i                                            
	OSX.Mdropper            1    i                                            
	OSX.RSPlug              3    A                                            
	OSX.MaControl           1    i                                            
	OSX.Leverage            1    a                                            
	OSX.MacDefender        35    A, B, CDE, F, G, HI, J, K, L, M, N, O        
	OSX.AdPlugin2           1    i                                            
	OSX.FileSteal           2    i                                            
	OSX.Revir               4    A, ii, iii, iv                               
	OSX.eicar.com           1    i                                            
	OSX.Iservice            2    A, B                                         
	OSX.FlashBack          24    A, B, C                                      
	OSX.AdPlugin            1    i                                            
	OSX.QHost.WB            2    A                                            
	OSX.DevilRobber         5    A, B                                         
	OSX.OpinionSpy          1                                                 
	18 threats, 37 variants, 93 signatures (version 69).

