#include "clock.h"

//                                 
//             ########            
//           ############          
//         ####        ####        
//        ###            ###       
//       ##       ##       ##      
//      ##                  ##     
//     ##    #          #    ##    
//    ##          ##          ##   
//    ##          ##          ##   
//   ##   #       ##       #   ##  
//   ##           ##           ##  
//  ##            ##            ## 
//  ##            ##            ## 
//  ##            ##            ## 
//  ##  #         ######     #  ## 
//  ##  #         ######     #  ## 
//  ##                          ## 
//  ##                          ## 
//  ##                          ## 
//   ##                        ##  
//   ##   #                #   ##  
//    ##                      ##   
//    ##                      ##   
//     ##    #          #    ##    
//      ##                  ##     
//       ##       ##       ##      
//        ###            ###       
//         ####        ####        
//           ############          
//             ########            
//                                 

	const uint8 clock.c_Array[] PROGMEM = {
		0x00, 0x00, 0x00, 0x00, 0x80, 0xC0, 0x60, 0x30, 0x18, 0x18, 0x8C, 0x0C, 0x06, 0x06, 0x06, 0x26, 0x26, 0x06, 0x06, 0x06, 0x0C, 0x8C, 0x18, 0x18, 0x30, 0x60, 0xC0, 0x80, 0x00, 0x00, 0x00, 0x00, 
		0x00, 0xF0, 0xFC, 0x0F, 0x03, 0x80, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00, 0x00, 0x04, 0x00, 0x80, 0x03, 0x0F, 0xFC, 0xF0, 0x00, 
		0x00, 0x0F, 0x3F, 0xF0, 0xC0, 0x01, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x20, 0x00, 0x01, 0xC0, 0xF0, 0x3F, 0x0F, 0x00, 
		0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x06, 0x0C, 0x18, 0x18, 0x31, 0x30, 0x60, 0x60, 0x60, 0x64, 0x64, 0x60, 0x60, 0x60, 0x30, 0x31, 0x18, 0x18, 0x0C, 0x06, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 
	};

	const bitmap clock.c PROGMEM = {
		.Height = 31,
		.Width  = 31,
		.Array  = clock.c_Array,
	};
