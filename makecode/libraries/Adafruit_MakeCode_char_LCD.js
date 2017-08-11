// some string blocks to be used with the char lcd
namespace str {
    //% blockNamespace=strings inBasicCategory=true
    //% blockId=to_string block="number to string|%num" blockGap=8
    export function to_string(num : number){
        return num.toString()
    }

    //% blockNamespace=strings inBasicCategory=true
    //% blockId=string_concat block="add two strings together|%str0|%str1"
    export function str_concat(str0 : string, str1 : string){
	  return str0 + str1
    }

    //% blockNamespace=strings inBasicCategory=true
    //% blockId=cut_str block="shorten string|%str by|%value places"
    export function cut_str(str : string, num : number){
    	   let ret = ""
	   for(let i = 0; i < num; i++){
		ret += str.charAt(i)
	   }
	   return ret
    }

    //% blockNamespace=strings inBasicCategory=true
    //% blockId=find_first block="find first occurence|%str by|%cha character"
    export function find_first_oc(str :  string, cha : string){
		for(let i = 0; i < str.length; i++){
			if(str.charAt(i) == cha)return i
		}
		return -1
    }
}

namespace char_lcd {
    let LCD_CLEARDISPLAY        = 0x01
    let LCD_RETURNHOME          = 0x02
    let LCD_ENTRYMODESET        = 0x04
    let LCD_DISPLAYCONTROL      = 0x08
    let LCD_CURSORSHIFT         = 0x10
    let LCD_FUNCTIONSET         = 0x20
    let LCD_SETCGRAMADDR        = 0x40
    let LCD_SETDDRAMADDR        = 0x80
    // Entry flags
    let LCD_ENTRYRIGHT          = 0x00
    let LCD_ENTRYLEFT           = 0x02
    let LCD_ENTRYSHIFTINCREMENT = 0x01
    let LCD_ENTRYSHIFTDECREMENT = 0x00
    // Control flags
    let LCD_DISPLAYON           = 0x04
    let LCD_DISPLAYOFF          = 0x00
    let LCD_CURSORON            = 0x02
    let LCD_CURSOROFF           = 0x00
    let LCD_BLINKON             = 0x01
    let LCD_BLINKOFF            = 0x00
    // Move flags
    let LCD_DISPLAYMOVE         = 0x08
    let LCD_CURSORMOVE          = 0x00
    let LCD_MOVERIGHT           = 0x04
    let LCD_MOVELEFT            = 0x00
    // Function set flags
    let LCD_8BITMODE            = 0x10
    let LCD_4BITMODE            = 0x00
    let LCD_2LINE               = 0x08
    let LCD_1LINE               = 0x00
    let LCD_5x10DOTS            = 0x04
    let LCD_5x8DOTS             = 0x00

    let rs : DigitalPin
    let en : DigitalPin
    let d7 : DigitalPin
    let d6 : DigitalPin
    let d5 : DigitalPin
    let d4 : DigitalPin
    let backlight : DigitalPin

    //% blockNamespace=lcd inBasicCategory=true
    //% blockId=char_lcd_setup block="set up lcd|%rs|%en|%d7|%d6|%d5|%d4|%bl" bockGap=8
    //export function setup_lcd(_rs : DigitalPin, _en : DigitalPin, _d7 : DigitalPin, _d6 : DigitalPin, _d5 : DigitalPin, _d4 : DigitalPin, _backlight : DigitalPin){
    export function setup_lcd(_rs : DigitalPin, _en : DigitalPin, _d4 : DigitalPin, _d5 : DigitalPin, _d6 : DigitalPin, _d7 : DigitalPin, _backlight : DigitalPin){
    	  rs = _rs
	  en = _en
	  d4 = _d4
	  d5 = _d5
	  d6 = _d6
	  d7 = _d7
	  backlight = _backlight
	  write_8(0x33, false)
	  write_8(0x32, false)
	  write_8((LCD_DISPLAYCONTROL | (LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF)), false)
    }
    export function write_8(value: number, char_mode: boolean) {
        loops.pause(1000 * .001)
        rs.digitalWrite(char_mode)
        // upper 4 bits
        d4.digitalWrite(((value >> 4) & 1) > 0)
        d5.digitalWrite(((value >> 5) & 1) > 0)
        d6.digitalWrite(((value >> 6) & 1) > 0)
        d7.digitalWrite(((value >> 7) & 1) > 0)
        // send command
        pulse_enable(true)
        d4.digitalWrite((value & 1) > 0)
        d5.digitalWrite(((value >> 1) & 1) > 0)
        d6.digitalWrite(((value >> 2) & 1) > 0)
        d7.digitalWrite(((value >> 3) & 1) > 0)
        pulse_enable(false)
    }
    export function pulse_enable(tr: boolean) {
        en.digitalWrite(false)
        loops.pause(0.0001)
        en.digitalWrite(true)
        loops.pause(0.0001)
        en.digitalWrite(false)
        loops.pause(0.0001)
    }
    //% blockNamespace=lcd inBasicCategory=true
    //% blockId=char_lcd_clear block="clear lcd" blockGap=8
    export function clear() {
        write_8(LCD_CLEARDISPLAY, false)
        loops.pause(1000 * .003)
    }

    //% blockNamespace=lcd inBasicCategory=true
    //% blockId=round_num block="round a number|%num"
    export function round_num(num : number){
	  return Math.round(num)
    }

    //% blockNamespace=lcd inBasicCategory=true
    //% blockId=char_lcd_message block="write to LCD|line 1:%line0|line 2:%line1" blockGap=8
    export function message(l0: string, l1: string) {
    	  let text = (l0 + '›' + l1)
        let i = 0
        for (i = 0; i < text.length; i++) {
            //if (text.charAt(i) == '\n') { // didn't work
		// '›' shift+alt+4 on mac acts as newline
            if (text.charAt(i) == '›') {
                //write_8(LCD_SETDDRAMADDR | (col + LCD_ROW_OFFSETS[row]))
                //write_8((LCD_SETDDRAMADDR | (0+LCD_ROW_OFFSETS[1])), false)
                write_8((LCD_SETDDRAMADDR | 64), false)
            }
            else {
		    write_8(text.charCodeAt(i), true)
            }
        }
    }
}
