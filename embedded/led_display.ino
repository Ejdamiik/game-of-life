#include "display.h"
#include <SPI.h>

// Pin definitions for MAX7219
const int DIN_PIN = 23;  // Data In
const int CS_PIN = 5;   // Chip Select
const int CLK_PIN = 18;  // Clock

// Initialize the LedControl library
// Parameters: DataIn, Clock, Load(CS), Number of MAX7219 devices
ExtendedDisplay display = ExtendedDisplay(DIN_PIN, CLK_PIN, CS_PIN, 4);

void setup()
{
  // Initialize the MAX7219 device
  display.shutdown(false);       // Wake up the MAX7219 from power-saving mode
  display.setIntensity(8);       // Set brightness level (0 is min, 15 is max)
  display.clearDisplay();          // Clear the display

  for (int row = 0; row < 8; row++)
  {
    for (int col = 0; col < 32; col++)
    {
      display.setLed(row, col, true);
      delay(500);
      display.setLed(row, col, false);
    }
  }
}

void loop()
{
}
