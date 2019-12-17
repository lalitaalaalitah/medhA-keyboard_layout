........................................................................................
1. add this to evdev.xml
........................................................................................ 

      <variant>          
        <configItem>            
          <name>sa</name>            
          <description>sanskrit</description>            
          <languageList>                                      
            <iso639Id>sa</iso639Id>                          
          </languageList>          
        </configItem>        
      </variant>


........................................................................................
2. Open termial and run this as superuser
    ........................................
    setxkbmap -layout 'us,sa'
    ........................................
........................................................................................
3. Set switching keys in keyboard options.
