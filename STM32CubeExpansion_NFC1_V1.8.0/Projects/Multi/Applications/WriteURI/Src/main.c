/**
  ******************************************************************************
  * @file    main.c
  * @author  AST Shared Innovation
 * @version	1.8.0
 * @date	10-October-2018
  * @brief   This file describe the main program.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; COPYRIGHT(c) 2016 STMicroelectronics</center></h2>
  *
  * Redistribution and use in source and binary forms, with or without modification,
  * are permitted provided that the following conditions are met:
  *   1. Redistributions of source code must retain the above copyright notice,
  *      this list of conditions and the following disclaimer.
  *   2. Redistributions in binary form must reproduce the above copyright notice,
  *      this list of conditions and the following disclaimer in the documentation
  *      and/or other materials provided with the distribution.
  *   3. Neither the name of STMicroelectronics nor the names of its contributors
  *      may be used to endorse or promote products derived from this software
  *      without specific prior written permission.
  *
  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
  * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
  */
	
/* 
 * This program is designed for a nucleo F4 board using HAL library. 
 * It uses the M24SR expansion board to check its functionalities. The program initialize 
 * the shield, then write an URL (http://www.st.com).
 */
 
 
 /**
   * @mainpage STM32Cube expansion software for X-NUCLEO-NFC01A1
   * <b>Introduction</b> <br>  
   * This firmware package includes Components Device Drivers, Board Support Package and a sample application demonstrating usage of X-NUCLEO-NFC01A1 expansion board alongwith SRM32 Nucleo boards. <br>
   *
   * <b>Sample Application Description</b><br>
   * The sample application configures M24SR(NFC tag type 4A) to transmit NDEF URL message to NFC compatible smartphone. It includes complete middleware to build applications running on STM32 using STM32Cube drivers. <br>
   *
   *
   * <b>Toolchain Support</b><br>
   * The firmware has been developed and tested on following toolchains:
   *	- IAR Embedded Workbench for ARM (EWARM) toolchain V8.20.1 + ST-Link
   *	- Keil Microcontroller Development Kit (MDK-ARM) toolchain V5.16a + ST-LINK
   *	- System Workbench for STM32 (SW4STM32) V2.4.0 + ST-LINK
   *
   * <b>How to use the firmware</b> <br>  
   * Please follow instructions mentioned in Projects\Multi\Applications\WriteURI\Binary\readme.txt <br>
   *   
  */
 
 
 
/* Includes ------------------------------------------------------------------*/
#include "main.h"


/** @addtogroup M24SR_Applications
  * @{
  */ 

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* I2C handler declaration */
I2C_HandleTypeDef hi2c1;

/* Private function prototypes -----------------------------------------------*/
static void Error_Handler(void);
static void initLED(void);

/* Private functions ---------------------------------------------------------*/

/**
  * @brief  Main program
  * @param  None
  * @retval None
  */
int main(void)
{    
  sURI_Info URI;
  /* Reset of all peripherals, Initializes the Flash interface and the systick. */
  HAL_Init();
  /* Configure the system clock */
  SystemClock_Config();
  
  // Init of the Nucleo Board led
  BSP_LED_Init(LED2);
	
  // Init of the M24SR expansion board
  initLED();
  
  // Init of the Type Tag 4 component (M24SR)
  // Thanks to a call to KillSession command during init no issue can occurs
  // If customer modify the code to avoid Kill session command call,
  // he must retry Init until succes (session can be lock by RF )
  while (TT4_Init() != SUCCESS);
  
  // Set the LED2 on to indicate Init done
  HAL_GPIO_WritePin(GPIOB,GPIO_PIN_5,GPIO_PIN_SET);
  
  // Prepare URI NDEF message content
  strcpy(URI.protocol,URI_ID_0x01_STRING);
  strcpy(URI.URI_Message,"st.com");
  strcpy(URI.Information,"\0");
  
  // First write NDEF
  while (TT4_WriteURI(&URI) != SUCCESS);
  
  // Set the LED3 on to indicate Programing done
  HAL_GPIO_WritePin(GPIOA,GPIO_PIN_10,GPIO_PIN_SET);
  
  while (1)
  {
    
  }
}

/**
  * @brief  I2C initialization for M24SR
  * @param  None
  * @retval None
  */
void M24SR_I2CInit ( void )
{
	/* check if we re-init after a detected issue */
	if( hi2c1.Instance == M24SR_I2C)
	  HAL_I2C_DeInit(&hi2c1);
	
  /* Configure I2C structure */
  hi2c1.Instance 	     = M24SR_I2C;
  hi2c1.Init.AddressingMode  = I2C_ADDRESSINGMODE_7BIT;
#if defined (STM32F302x8)
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
  hi2c1.Init.NoStretchMode   = I2C_NOSTRETCH_DISABLE;
#elif defined (STM32F401xE)
  hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLED;
  hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLED;
  hi2c1.Init.NoStretchMode   = I2C_NOSTRETCH_DISABLED;  
#endif  
  hi2c1.Init.OwnAddress1     = 0;
  hi2c1.Init.OwnAddress2     = 0;
#if (defined USE_STM32F4XX_NUCLEO) || (defined USE_STM32L1XX_NUCLEO) || \
	  (defined USE_STM32F1XX_NUCLEO)
  hi2c1.Init.ClockSpeed      = M24SR_I2C_SPEED;
  hi2c1.Init.DutyCycle       = I2C_DUTYCYCLE_2;
#elif (defined USE_STM32F0XX_NUCLEO) || (defined USE_STM32L0XX_NUCLEO) || \
      (defined USE_STM32F3XX_NUCLEO) || (defined USE_STM32L4XX_NUCLEO)
  hi2c1.Init.Timing          = M24SR_I2C_SPEED;
#endif
   
	if(HAL_I2C_Init(&hi2c1) != HAL_OK)
  {
    /* Initialization Error */
    Error_Handler();    
  }
	
}

/**
  * @brief  GPO initialization for M24SR
  * @param  None
  * @retval None
  */
void M24SR_GPOInit ( void )
{
  GPIO_InitTypeDef GPIO_InitStruct;
  
  /* GPIO Ports Clock Enable */
  INIT_CLK_GPO_RFD();
	
  /* Configure GPIO pins for GPO (PA6)*/
#ifndef I2C_GPO_INTERRUPT_ALLOWED
  GPIO_InitStruct.Pin = M24SR_GPO_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
  HAL_GPIO_Init(M24SR_GPO_PIN_PORT, &GPIO_InitStruct);
#else
  GPIO_InitStruct.Pin = M24SR_GPO_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL; 
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;

  HAL_GPIO_Init(M24SR_GPO_PIN_PORT, &GPIO_InitStruct);
  /* Enable and set EXTI9_5 Interrupt to the lowest priority */
#if (defined USE_STM32F4XX_NUCLEO) || (defined USE_STM32F3XX_NUCLEO) || \
     (defined USE_STM32L1XX_NUCLEO) || (defined USE_STM32F1XX_NUCLEO) || (defined USE_STM32L4XX_NUCLEO) 
  HAL_NVIC_SetPriority(EXTI9_5_IRQn, 3, 0);
  HAL_NVIC_EnableIRQ(EXTI9_5_IRQn);
#elif (defined USE_STM32L0XX_NUCLEO) || (defined USE_STM32F0XX_NUCLEO) 
  HAL_NVIC_SetPriority(EXTI4_15_IRQn, 3, 0);
  HAL_NVIC_EnableIRQ(EXTI4_15_IRQn);    
#endif
  
#endif
	
  /* Configure GPIO pins for DISABLE (PA7)*/
  GPIO_InitStruct.Pin = M24SR_RFDIS_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(M24SR_RFDIS_PIN_PORT, &GPIO_InitStruct);
}

/**
  * @brief  This function wait the time given in param (in milisecond)
	* @param	time_ms: time value in milisecond
  */
void M24SR_WaitMs(uint32_t time_ms)
{
	wait_ms(time_ms);
}

/**
  * @brief  This function retrieve current tick
  * @param	ptickstart: pointer on a variable to store current tick value
  */
void M24SR_GetTick( uint32_t *ptickstart )
{
	*ptickstart = HAL_GetTick();
}
/**
  * @brief  This function read the state of the M24SR GPO
	* @param	none
  * @retval GPIO_PinState : state of the M24SR GPO
  */
void M24SR_GPO_ReadPin( GPIO_PinState * pPinState)
{
	*pPinState = HAL_GPIO_ReadPin(M24SR_GPO_PIN_PORT,M24SR_GPO_PIN);
}

/**
  * @brief  This function set the state of the M24SR RF disable pin
	* @param	PinState: put RF disable pin of M24SR in PinState (1 or 0)
  */
void M24SR_RFDIS_WritePin( GPIO_PinState PinState)
{
	HAL_GPIO_WritePin(M24SR_RFDIS_PIN_PORT,M24SR_RFDIS_PIN,PinState);
}


/**
  * @brief  Intitialize the leds of the M24SR expansion board
  * @param  None
  * @retval None
  */
static void initLED(void)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  __GPIOA_CLK_ENABLE();
  __GPIOB_CLK_ENABLE();
  /* Configure GPIO for LEDs (PB4,PB5,PA10)*/
  GPIO_InitStruct.Pin = GPIO_PIN_4 | GPIO_PIN_5;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
#if (defined USE_STM32F4XX_NUCLEO) || (defined USE_STM32L4XX_NUCLEO)
  GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
#elif (defined USE_STM32L0XX_NUCLEO) || (defined USE_STM32F3XX_NUCLEO) || \
      (defined USE_STM32L1XX_NUCLEO) || (defined USE_STM32F1XX_NUCLEO) 
  GPIO_InitStruct.Speed = GPIO_SPEED_HIGH;
#elif (defined USE_STM32F0XX_NUCLEO) 
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;  
#endif  
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
  
  GPIO_InitStruct.Pin = GPIO_PIN_10;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);
}

/**
  * @brief  This function is executed in case of error occurrence.
  * @param  None
  * @retval None
  */
static void Error_Handler(void)
{
  /* Turn LED2 on */
  BSP_LED_On(LED2);
  while (1)
  {
  }
}


#ifdef  USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */

  /* Infinite loop */
  while (1)
  {
  }
}
#endif

/**
  * @}
  */ 

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
