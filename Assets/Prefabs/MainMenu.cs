using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class MainMenu : MonoBehaviour
{
    [SerializeField] GameObject MainMenuHolder;


    public void OnLetsGetStartedClicked()
    {
        this.MainMenuHolder.gameObject.SetActive(false);
    }
}
