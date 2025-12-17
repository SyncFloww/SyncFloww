export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export type Database = {
  // Allows to automatically instantiate createClient with right options
  // instead of createClient<Database, { PostgrestVersion: 'XX' }>(URL, KEY)
  __InternalSupabase: {
    PostgrestVersion: "13.0.5"
  }
  public: {
    Tables: {
      AIs_agenttask: {
        Row: {
          agent_id: number
          completed_at: string | null
          created_at: string
          id: number
          input_data: Json
          output_data: Json | null
          status: string
          updated_at: string
        }
        Insert: {
          agent_id: number
          completed_at?: string | null
          created_at: string
          id?: number
          input_data: Json
          output_data?: Json | null
          status: string
          updated_at: string
        }
        Update: {
          agent_id?: number
          completed_at?: string | null
          created_at?: string
          id?: number
          input_data?: Json
          output_data?: Json | null
          status?: string
          updated_at?: string
        }
        Relationships: [
          {
            foreignKeyName: "AIs_agenttask_agent_id_58844f4a_fk_AIs_aiagent_id"
            columns: ["agent_id"]
            isOneToOne: false
            referencedRelation: "AIs_aiagent"
            referencedColumns: ["id"]
          },
        ]
      }
      AIs_aiagent: {
        Row: {
          config: Json
          created_at: string
          description: string
          id: number
          is_active: boolean
          model_id: number
          name: string
          task_type: string
          updated_at: string
        }
        Insert: {
          config: Json
          created_at: string
          description: string
          id?: number
          is_active: boolean
          model_id: number
          name: string
          task_type: string
          updated_at: string
        }
        Update: {
          config?: Json
          created_at?: string
          description?: string
          id?: number
          is_active?: boolean
          model_id?: number
          name?: string
          task_type?: string
          updated_at?: string
        }
        Relationships: [
          {
            foreignKeyName: "AIs_aiagent_model_id_ce7ff5a9_fk_AIs_aimodel_id"
            columns: ["model_id"]
            isOneToOne: false
            referencedRelation: "AIs_aimodel"
            referencedColumns: ["id"]
          },
        ]
      }
      AIs_aiconfiguration: {
        Row: {
          created_at: string
          id: number
          is_active: boolean
          max_length: number
          model_name: string
          name: string
          temperature: number
          updated_at: string
          user_id: number
        }
        Insert: {
          created_at: string
          id?: number
          is_active: boolean
          max_length: number
          model_name: string
          name: string
          temperature: number
          updated_at: string
          user_id: number
        }
        Update: {
          created_at?: string
          id?: number
          is_active?: boolean
          max_length?: number
          model_name?: string
          name?: string
          temperature?: number
          updated_at?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "AIs_aiconfiguration_user_id_610ecba4_fk"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      AIs_aimodel: {
        Row: {
          context_window: number | null
          created_at: string
          description: string
          id: number
          is_active: boolean
          model_id: string
          model_type: string
          name: string
          provider_id: number
          updated_at: string
        }
        Insert: {
          context_window?: number | null
          created_at: string
          description: string
          id?: number
          is_active: boolean
          model_id: string
          model_type: string
          name: string
          provider_id: number
          updated_at: string
        }
        Update: {
          context_window?: number | null
          created_at?: string
          description?: string
          id?: number
          is_active?: boolean
          model_id?: string
          model_type?: string
          name?: string
          provider_id?: number
          updated_at?: string
        }
        Relationships: [
          {
            foreignKeyName: "AIs_aimodel_provider_id_f3b98908_fk_AIs_llmprovider_id"
            columns: ["provider_id"]
            isOneToOne: false
            referencedRelation: "AIs_llmprovider"
            referencedColumns: ["id"]
          },
        ]
      }
      AIs_llmprovider: {
        Row: {
          api_key: string | null
          base_url: string | null
          created_at: string
          id: number
          is_active: boolean
          name: string
          provider_class: string
          updated_at: string
        }
        Insert: {
          api_key?: string | null
          base_url?: string | null
          created_at: string
          id?: number
          is_active: boolean
          name: string
          provider_class: string
          updated_at: string
        }
        Update: {
          api_key?: string | null
          base_url?: string | null
          created_at?: string
          id?: number
          is_active?: boolean
          name?: string
          provider_class?: string
          updated_at?: string
        }
        Relationships: []
      }
      analytics_analyticsdata: {
        Row: {
          comments: number
          created_at: string
          date: string
          followers: number
          following: number
          id: number
          impressions: number
          likes: number
          profile_views: number
          reach: number
          shares: number
          social_account_id: number
          updated_at: string
          website_clicks: number
        }
        Insert: {
          comments: number
          created_at: string
          date: string
          followers: number
          following: number
          id?: number
          impressions: number
          likes: number
          profile_views: number
          reach: number
          shares: number
          social_account_id: number
          updated_at: string
          website_clicks: number
        }
        Update: {
          comments?: number
          created_at?: string
          date?: string
          followers?: number
          following?: number
          id?: number
          impressions?: number
          likes?: number
          profile_views?: number
          reach?: number
          shares?: number
          social_account_id?: number
          updated_at?: string
          website_clicks?: number
        }
        Relationships: [
          {
            foreignKeyName: "analytics_analyticsd_social_account_id_6d0a550c_fk_social_so"
            columns: ["social_account_id"]
            isOneToOne: false
            referencedRelation: "social_socialaccount"
            referencedColumns: ["id"]
          },
        ]
      }
      auth_group: {
        Row: {
          id: number
          name: string
        }
        Insert: {
          id?: number
          name: string
        }
        Update: {
          id?: number
          name?: string
        }
        Relationships: []
      }
      auth_group_permissions: {
        Row: {
          group_id: number
          id: number
          permission_id: number
        }
        Insert: {
          group_id: number
          id?: number
          permission_id: number
        }
        Update: {
          group_id?: number
          id?: number
          permission_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm"
            columns: ["permission_id"]
            isOneToOne: false
            referencedRelation: "auth_permission"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id"
            columns: ["group_id"]
            isOneToOne: false
            referencedRelation: "auth_group"
            referencedColumns: ["id"]
          },
        ]
      }
      auth_permission: {
        Row: {
          codename: string
          content_type_id: number
          id: number
          name: string
        }
        Insert: {
          codename: string
          content_type_id: number
          id?: number
          name: string
        }
        Update: {
          codename?: string
          content_type_id?: number
          id?: number
          name?: string
        }
        Relationships: [
          {
            foreignKeyName: "auth_permission_content_type_id_2f476e4b_fk_django_co"
            columns: ["content_type_id"]
            isOneToOne: false
            referencedRelation: "django_content_type"
            referencedColumns: ["id"]
          },
        ]
      }
      automations_agenttask: {
        Row: {
          agent_id: number
          completed_at: string | null
          created_at: string
          id: number
          input_data: Json | null
          status: string
          updated_at: string
        }
        Insert: {
          agent_id: number
          completed_at?: string | null
          created_at: string
          id?: number
          input_data?: Json | null
          status: string
          updated_at: string
        }
        Update: {
          agent_id?: number
          completed_at?: string | null
          created_at?: string
          id?: number
          input_data?: Json | null
          status?: string
          updated_at?: string
        }
        Relationships: [
          {
            foreignKeyName: "automations_agenttas_agent_id_5fffb13e_fk_automatio"
            columns: ["agent_id"]
            isOneToOne: false
            referencedRelation: "automations_aiagent"
            referencedColumns: ["id"]
          },
        ]
      }
      automations_aiagent: {
        Row: {
          description: string
          id: number
          is_active: boolean
          model_id: number
          name: string
          task_type: string
        }
        Insert: {
          description: string
          id?: number
          is_active: boolean
          model_id: number
          name: string
          task_type: string
        }
        Update: {
          description?: string
          id?: number
          is_active?: boolean
          model_id?: number
          name?: string
          task_type?: string
        }
        Relationships: [
          {
            foreignKeyName: "automations_aiagent_model_id_1fd5aa15_fk_automations_aimodel_id"
            columns: ["model_id"]
            isOneToOne: false
            referencedRelation: "automations_aimodel"
            referencedColumns: ["id"]
          },
        ]
      }
      automations_aimodel: {
        Row: {
          description: string
          id: number
          is_active: boolean
          model_id: string
          model_type: string
          name: string
          provider_id: number
        }
        Insert: {
          description: string
          id?: number
          is_active: boolean
          model_id: string
          model_type: string
          name: string
          provider_id: number
        }
        Update: {
          description?: string
          id?: number
          is_active?: boolean
          model_id?: string
          model_type?: string
          name?: string
          provider_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "automations_aimodel_provider_id_84c856ef_fk_automatio"
            columns: ["provider_id"]
            isOneToOne: false
            referencedRelation: "automations_llmprovider"
            referencedColumns: ["id"]
          },
        ]
      }
      automations_automationrule: {
        Row: {
          automation_type: string
          created_at: string
          daily_limit: number
          id: number
          interval_minutes: number
          is_active: boolean
          message: string
          name: string
          social_account_id: number
          status: string
          target: string
          updated_at: string
          user_id: number
        }
        Insert: {
          automation_type: string
          created_at: string
          daily_limit: number
          id?: number
          interval_minutes: number
          is_active: boolean
          message: string
          name: string
          social_account_id: number
          status: string
          target: string
          updated_at: string
          user_id: number
        }
        Update: {
          automation_type?: string
          created_at?: string
          daily_limit?: number
          id?: number
          interval_minutes?: number
          is_active?: boolean
          message?: string
          name?: string
          social_account_id?: number
          status?: string
          target?: string
          updated_at?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "automations_automati_social_account_id_97541a88_fk_social_so"
            columns: ["social_account_id"]
            isOneToOne: false
            referencedRelation: "social_socialaccount"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "automations_automati_user_id_7222262d_fk_UserAccou"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      automations_llmprovider: {
        Row: {
          api_key_env: string
          base_url: string
          id: number
          is_active: boolean
          name: string
          provider_class: string
        }
        Insert: {
          api_key_env: string
          base_url: string
          id?: number
          is_active: boolean
          name: string
          provider_class: string
        }
        Update: {
          api_key_env?: string
          base_url?: string
          id?: number
          is_active?: boolean
          name?: string
          provider_class?: string
        }
        Relationships: []
      }
      campaigns_emailcampaign: {
        Row: {
          content: string
          created_at: string
          id: number
          name: string
          recipient_list: string
          scheduled_time: string | null
          sent_time: string | null
          status: string
          subject: string
          updated_at: string
          user_id: number
        }
        Insert: {
          content: string
          created_at: string
          id?: number
          name: string
          recipient_list: string
          scheduled_time?: string | null
          sent_time?: string | null
          status: string
          subject: string
          updated_at: string
          user_id: number
        }
        Update: {
          content?: string
          created_at?: string
          id?: number
          name?: string
          recipient_list?: string
          scheduled_time?: string | null
          sent_time?: string | null
          status?: string
          subject?: string
          updated_at?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "campaigns_emailcampaign_user_id_20f933bb_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      contents_content: {
        Row: {
          content_type: string
          created_at: string
          id: number
          media: string | null
          published_time: string | null
          scheduled_time: string | null
          status: string
          text: string
          title: string
          updated_at: string
          user_id: number
        }
        Insert: {
          content_type: string
          created_at: string
          id?: number
          media?: string | null
          published_time?: string | null
          scheduled_time?: string | null
          status: string
          text: string
          title: string
          updated_at: string
          user_id: number
        }
        Update: {
          content_type?: string
          created_at?: string
          id?: number
          media?: string | null
          published_time?: string | null
          scheduled_time?: string | null
          status?: string
          text?: string
          title?: string
          updated_at?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "contents_content_user_id_90dae091_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      contents_content_social_accounts: {
        Row: {
          content_id: number
          id: number
          socialaccount_id: number
        }
        Insert: {
          content_id: number
          id?: number
          socialaccount_id: number
        }
        Update: {
          content_id?: number
          id?: number
          socialaccount_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "contents_content_soc_content_id_8760acd9_fk_contents_"
            columns: ["content_id"]
            isOneToOne: false
            referencedRelation: "contents_content"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "contents_content_soc_socialaccount_id_ead10df0_fk_social_so"
            columns: ["socialaccount_id"]
            isOneToOne: false
            referencedRelation: "social_socialaccount"
            referencedColumns: ["id"]
          },
        ]
      }
      core_brand: {
        Row: {
          created_at: string
          description: string
          id: number
          logo: string | null
          name: string
          updated_at: string
          user_id: number
          website: string
        }
        Insert: {
          created_at: string
          description: string
          id?: number
          logo?: string | null
          name: string
          updated_at: string
          user_id: number
          website: string
        }
        Update: {
          created_at?: string
          description?: string
          id?: number
          logo?: string | null
          name?: string
          updated_at?: string
          user_id?: number
          website?: string
        }
        Relationships: [
          {
            foreignKeyName: "core_brand_user_id_3d37a223_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      django_admin_log: {
        Row: {
          action_flag: number
          action_time: string
          change_message: string
          content_type_id: number | null
          id: number
          object_id: string | null
          object_repr: string
          user_id: number
        }
        Insert: {
          action_flag: number
          action_time: string
          change_message: string
          content_type_id?: number | null
          id?: number
          object_id?: string | null
          object_repr: string
          user_id: number
        }
        Update: {
          action_flag?: number
          action_time?: string
          change_message?: string
          content_type_id?: number | null
          id?: number
          object_id?: string | null
          object_repr?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "django_admin_log_content_type_id_c4bce8eb_fk_django_co"
            columns: ["content_type_id"]
            isOneToOne: false
            referencedRelation: "django_content_type"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "django_admin_log_user_id_c564eba6_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      django_celery_beat_clockedschedule: {
        Row: {
          clocked_time: string
          id: number
        }
        Insert: {
          clocked_time: string
          id?: number
        }
        Update: {
          clocked_time?: string
          id?: number
        }
        Relationships: []
      }
      django_celery_beat_crontabschedule: {
        Row: {
          day_of_month: string
          day_of_week: string
          hour: string
          id: number
          minute: string
          month_of_year: string
          timezone: string
        }
        Insert: {
          day_of_month: string
          day_of_week: string
          hour: string
          id?: number
          minute: string
          month_of_year: string
          timezone: string
        }
        Update: {
          day_of_month?: string
          day_of_week?: string
          hour?: string
          id?: number
          minute?: string
          month_of_year?: string
          timezone?: string
        }
        Relationships: []
      }
      django_celery_beat_intervalschedule: {
        Row: {
          every: number
          id: number
          period: string
        }
        Insert: {
          every: number
          id?: number
          period: string
        }
        Update: {
          every?: number
          id?: number
          period?: string
        }
        Relationships: []
      }
      django_celery_beat_periodictask: {
        Row: {
          args: string
          clocked_id: number | null
          crontab_id: number | null
          date_changed: string
          description: string
          enabled: boolean
          exchange: string | null
          expire_seconds: number | null
          expires: string | null
          headers: string
          id: number
          interval_id: number | null
          kwargs: string
          last_run_at: string | null
          name: string
          one_off: boolean
          priority: number | null
          queue: string | null
          routing_key: string | null
          solar_id: number | null
          start_time: string | null
          task: string
          total_run_count: number
        }
        Insert: {
          args: string
          clocked_id?: number | null
          crontab_id?: number | null
          date_changed: string
          description: string
          enabled: boolean
          exchange?: string | null
          expire_seconds?: number | null
          expires?: string | null
          headers: string
          id?: number
          interval_id?: number | null
          kwargs: string
          last_run_at?: string | null
          name: string
          one_off: boolean
          priority?: number | null
          queue?: string | null
          routing_key?: string | null
          solar_id?: number | null
          start_time?: string | null
          task: string
          total_run_count: number
        }
        Update: {
          args?: string
          clocked_id?: number | null
          crontab_id?: number | null
          date_changed?: string
          description?: string
          enabled?: boolean
          exchange?: string | null
          expire_seconds?: number | null
          expires?: string | null
          headers?: string
          id?: number
          interval_id?: number | null
          kwargs?: string
          last_run_at?: string | null
          name?: string
          one_off?: boolean
          priority?: number | null
          queue?: string | null
          routing_key?: string | null
          solar_id?: number | null
          start_time?: string | null
          task?: string
          total_run_count?: number
        }
        Relationships: [
          {
            foreignKeyName: "django_celery_beat_p_clocked_id_47a69f82_fk_django_ce"
            columns: ["clocked_id"]
            isOneToOne: false
            referencedRelation: "django_celery_beat_clockedschedule"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "django_celery_beat_p_crontab_id_d3cba168_fk_django_ce"
            columns: ["crontab_id"]
            isOneToOne: false
            referencedRelation: "django_celery_beat_crontabschedule"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "django_celery_beat_p_interval_id_a8ca27da_fk_django_ce"
            columns: ["interval_id"]
            isOneToOne: false
            referencedRelation: "django_celery_beat_intervalschedule"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "django_celery_beat_p_solar_id_a87ce72c_fk_django_ce"
            columns: ["solar_id"]
            isOneToOne: false
            referencedRelation: "django_celery_beat_solarschedule"
            referencedColumns: ["id"]
          },
        ]
      }
      django_celery_beat_periodictasks: {
        Row: {
          ident: number
          last_update: string
        }
        Insert: {
          ident: number
          last_update: string
        }
        Update: {
          ident?: number
          last_update?: string
        }
        Relationships: []
      }
      django_celery_beat_solarschedule: {
        Row: {
          event: string
          id: number
          latitude: number
          longitude: number
        }
        Insert: {
          event: string
          id?: number
          latitude: number
          longitude: number
        }
        Update: {
          event?: string
          id?: number
          latitude?: number
          longitude?: number
        }
        Relationships: []
      }
      django_content_type: {
        Row: {
          app_label: string
          id: number
          model: string
        }
        Insert: {
          app_label: string
          id?: number
          model: string
        }
        Update: {
          app_label?: string
          id?: number
          model?: string
        }
        Relationships: []
      }
      django_migrations: {
        Row: {
          app: string
          applied: string
          id: number
          name: string
        }
        Insert: {
          app: string
          applied: string
          id?: number
          name: string
        }
        Update: {
          app?: string
          applied?: string
          id?: number
          name?: string
        }
        Relationships: []
      }
      django_session: {
        Row: {
          expire_date: string
          session_data: string
          session_key: string
        }
        Insert: {
          expire_date: string
          session_data: string
          session_key: string
        }
        Update: {
          expire_date?: string
          session_data?: string
          session_key?: string
        }
        Relationships: []
      }
      django_site: {
        Row: {
          domain: string
          id: number
          name: string
        }
        Insert: {
          domain: string
          id?: number
          name: string
        }
        Update: {
          domain?: string
          id?: number
          name?: string
        }
        Relationships: []
      }
      profiles: {
        Row: {
          avatar_url: string | null
          created_at: string
          full_name: string | null
          id: string
          updated_at: string
          user_id: string
        }
        Insert: {
          avatar_url?: string | null
          created_at?: string
          full_name?: string | null
          id?: string
          updated_at?: string
          user_id: string
        }
        Update: {
          avatar_url?: string | null
          created_at?: string
          full_name?: string | null
          id?: string
          updated_at?: string
          user_id?: string
        }
        Relationships: []
      }
      projects: {
        Row: {
          created_at: string
          description: string | null
          generations_count: number | null
          id: string
          project_type: string
          status: string | null
          thumbnail_url: string | null
          title: string
          updated_at: string
          user_id: string
        }
        Insert: {
          created_at?: string
          description?: string | null
          generations_count?: number | null
          id?: string
          project_type: string
          status?: string | null
          thumbnail_url?: string | null
          title: string
          updated_at?: string
          user_id: string
        }
        Update: {
          created_at?: string
          description?: string | null
          generations_count?: number | null
          id?: string
          project_type?: string
          status?: string | null
          thumbnail_url?: string | null
          title?: string
          updated_at?: string
          user_id?: string
        }
        Relationships: []
      }
      social_auth_association: {
        Row: {
          assoc_type: string
          handle: string
          id: number
          issued: number
          lifetime: number
          secret: string
          server_url: string
        }
        Insert: {
          assoc_type: string
          handle: string
          id?: number
          issued: number
          lifetime: number
          secret: string
          server_url: string
        }
        Update: {
          assoc_type?: string
          handle?: string
          id?: number
          issued?: number
          lifetime?: number
          secret?: string
          server_url?: string
        }
        Relationships: []
      }
      social_auth_code: {
        Row: {
          code: string
          email: string
          id: number
          timestamp: string
          verified: boolean
        }
        Insert: {
          code: string
          email: string
          id?: number
          timestamp: string
          verified: boolean
        }
        Update: {
          code?: string
          email?: string
          id?: number
          timestamp?: string
          verified?: boolean
        }
        Relationships: []
      }
      social_auth_nonce: {
        Row: {
          id: number
          salt: string
          server_url: string
          timestamp: number
        }
        Insert: {
          id?: number
          salt: string
          server_url: string
          timestamp: number
        }
        Update: {
          id?: number
          salt?: string
          server_url?: string
          timestamp?: number
        }
        Relationships: []
      }
      social_auth_partial: {
        Row: {
          backend: string
          data: Json
          id: number
          next_step: number
          timestamp: string
          token: string
        }
        Insert: {
          backend: string
          data: Json
          id?: number
          next_step: number
          timestamp: string
          token: string
        }
        Update: {
          backend?: string
          data?: Json
          id?: number
          next_step?: number
          timestamp?: string
          token?: string
        }
        Relationships: []
      }
      social_auth_usersocialauth: {
        Row: {
          created: string
          extra_data: Json
          id: number
          modified: string
          provider: string
          uid: string
          user_id: number
        }
        Insert: {
          created: string
          extra_data: Json
          id?: number
          modified: string
          provider: string
          uid: string
          user_id: number
        }
        Update: {
          created?: string
          extra_data?: Json
          id?: number
          modified?: string
          provider?: string
          uid?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "social_auth_usersoci_user_id_17d28448_fk_UserAccou"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      social_scheduledpost: {
        Row: {
          brand_id: number | null
          content: string
          created_at: string
          id: number
          is_published: boolean
          media: string | null
          published_at: string | null
          scheduled_time: string
          updated_at: string
          user_id: number
        }
        Insert: {
          brand_id?: number | null
          content: string
          created_at: string
          id?: number
          is_published: boolean
          media?: string | null
          published_at?: string | null
          scheduled_time: string
          updated_at: string
          user_id: number
        }
        Update: {
          brand_id?: number | null
          content?: string
          created_at?: string
          id?: number
          is_published?: boolean
          media?: string | null
          published_at?: string | null
          scheduled_time?: string
          updated_at?: string
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "social_scheduledpost_brand_id_45a7871a_fk_core_brand_id"
            columns: ["brand_id"]
            isOneToOne: false
            referencedRelation: "core_brand"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "social_scheduledpost_user_id_0c932791_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      social_scheduledpost_social_accounts: {
        Row: {
          id: number
          scheduledpost_id: number
          socialaccount_id: number
        }
        Insert: {
          id?: number
          scheduledpost_id: number
          socialaccount_id: number
        }
        Update: {
          id?: number
          scheduledpost_id?: number
          socialaccount_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "social_scheduledpost_scheduledpost_id_c0ad9a3c_fk_social_sc"
            columns: ["scheduledpost_id"]
            isOneToOne: false
            referencedRelation: "social_scheduledpost"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "social_scheduledpost_socialaccount_id_00c8672f_fk_social_so"
            columns: ["socialaccount_id"]
            isOneToOne: false
            referencedRelation: "social_socialaccount"
            referencedColumns: ["id"]
          },
        ]
      }
      social_socialaccount: {
        Row: {
          access_token: string
          brand_id: number
          created_at: string
          extra_data: Json
          id: number
          provider: string
          uid: string
        }
        Insert: {
          access_token: string
          brand_id: number
          created_at: string
          extra_data: Json
          id?: number
          provider: string
          uid: string
        }
        Update: {
          access_token?: string
          brand_id?: number
          created_at?: string
          extra_data?: Json
          id?: number
          provider?: string
          uid?: string
        }
        Relationships: [
          {
            foreignKeyName: "social_socialaccount_brand_id_dc318998_fk_core_brand_id"
            columns: ["brand_id"]
            isOneToOne: false
            referencedRelation: "core_brand"
            referencedColumns: ["id"]
          },
        ]
      }
      status_status: {
        Row: {
          content: string
          date_published: string
          id: number
          user_id: number
        }
        Insert: {
          content: string
          date_published: string
          id?: number
          user_id: number
        }
        Update: {
          content?: string
          date_published?: string
          id?: number
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "status_status_user_id_a16a4ddb_fk_UserAccount_user_id"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      UserAccount_user: {
        Row: {
          date_joined: string
          email: string
          first_name: string
          id: number
          is_active: boolean
          is_staff: boolean
          is_superuser: boolean
          last_login: string | null
          last_name: string
          password: string
        }
        Insert: {
          date_joined: string
          email: string
          first_name: string
          id?: number
          is_active: boolean
          is_staff: boolean
          is_superuser: boolean
          last_login?: string | null
          last_name: string
          password: string
        }
        Update: {
          date_joined?: string
          email?: string
          first_name?: string
          id?: number
          is_active?: boolean
          is_staff?: boolean
          is_superuser?: boolean
          last_login?: string | null
          last_name?: string
          password?: string
        }
        Relationships: []
      }
      UserAccount_user_groups: {
        Row: {
          group_id: number
          id: number
          user_id: number
        }
        Insert: {
          group_id: number
          id?: number
          user_id: number
        }
        Update: {
          group_id?: number
          id?: number
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "UserAccount_user_groups_group_id_00747633_fk_auth_group_id"
            columns: ["group_id"]
            isOneToOne: false
            referencedRelation: "auth_group"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "UserAccount_user_groups_user_id_7e8af118_fk"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
      UserAccount_user_user_permissions: {
        Row: {
          id: number
          permission_id: number
          user_id: number
        }
        Insert: {
          id?: number
          permission_id: number
          user_id: number
        }
        Update: {
          id?: number
          permission_id?: number
          user_id?: number
        }
        Relationships: [
          {
            foreignKeyName: "UserAccount_user_use_permission_id_dfef7d28_fk_auth_perm"
            columns: ["permission_id"]
            isOneToOne: false
            referencedRelation: "auth_permission"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "UserAccount_user_user_permissions_user_id_05a56557_fk"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "UserAccount_user"
            referencedColumns: ["id"]
          },
        ]
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      [_ in never]: never
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

type DatabaseWithoutInternals = Omit<Database, "__InternalSupabase">

type DefaultSchema = DatabaseWithoutInternals[Extract<keyof Database, "public">]

export type Tables<
  DefaultSchemaTableNameOrOptions extends
    | keyof (DefaultSchema["Tables"] & DefaultSchema["Views"])
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
        DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
      DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : DefaultSchemaTableNameOrOptions extends keyof (DefaultSchema["Tables"] &
        DefaultSchema["Views"])
    ? (DefaultSchema["Tables"] &
        DefaultSchema["Views"])[DefaultSchemaTableNameOrOptions] extends {
        Row: infer R
      }
      ? R
      : never
    : never

export type TablesInsert<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Insert: infer I
      }
      ? I
      : never
    : never

export type TablesUpdate<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Update: infer U
      }
      ? U
      : never
    : never

export type Enums<
  DefaultSchemaEnumNameOrOptions extends
    | keyof DefaultSchema["Enums"]
    | { schema: keyof DatabaseWithoutInternals },
  EnumName extends DefaultSchemaEnumNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"]
    : never = never,
> = DefaultSchemaEnumNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : DefaultSchemaEnumNameOrOptions extends keyof DefaultSchema["Enums"]
    ? DefaultSchema["Enums"][DefaultSchemaEnumNameOrOptions]
    : never

export type CompositeTypes<
  PublicCompositeTypeNameOrOptions extends
    | keyof DefaultSchema["CompositeTypes"]
    | { schema: keyof DatabaseWithoutInternals },
  CompositeTypeName extends PublicCompositeTypeNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"]
    : never = never,
> = PublicCompositeTypeNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"][CompositeTypeName]
  : PublicCompositeTypeNameOrOptions extends keyof DefaultSchema["CompositeTypes"]
    ? DefaultSchema["CompositeTypes"][PublicCompositeTypeNameOrOptions]
    : never

export const Constants = {
  public: {
    Enums: {},
  },
} as const
